// lib/config/di/injection_container.dart
import 'package:dio/dio.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import 'package:get_it/get_it.dart';

import '../../core/network/dio_client.dart';
import '../../core/network/interceptors/auth_interceptor.dart';
import '../../core/network/interceptors/logging_interceptor.dart';
import '../../features/auth/data/datasources/auth_remote_data_source.dart';
import '../../features/auth/data/repositories/auth_repository_impl.dart';
import '../../features/auth/domain/repositories/auth_repository.dart';
import '../../features/auth/domain/usecases/login_usecase.dart';
import '../../features/auth/presentation/blocs/auth_bloc.dart';

final sl = GetIt.instance;

Future<void> initDependencies() async {
  _initExternal();
  _initCore();
  _initAuth();
}

void _initExternal() {
  sl.registerLazySingleton<FlutterSecureStorage>(
    () => const FlutterSecureStorage(),
  );
}

void _initCore() {
  sl.registerLazySingleton<DioClient>(() {
    final dio = Dio()
      ..interceptors.addAll([
        AuthInterceptor(sl<FlutterSecureStorage>()),
        LoggingInterceptor(), // solo imprime en kDebugMode internamente
      ]);

    return DioClient(existingDio: dio, authInterceptor: AuthInterceptor(sl<FlutterSecureStorage>()));
  });
}

void _initAuth() {
  sl.registerLazySingleton<AuthRemoteDataSource>(
    () => AuthRemoteDataSourceImpl(
      sl<DioClient>(),
      sl<FlutterSecureStorage>(),
    ),
  );

  sl.registerLazySingleton<AuthRepository>(
    () => AuthRepositoryImpl(sl<AuthRemoteDataSource>()),
  );

  sl.registerLazySingleton(() => LoginUseCase(sl<AuthRepository>()));

  sl.registerFactory(
    () => AuthBloc(loginUseCase: sl<LoginUseCase>()),
  );
}