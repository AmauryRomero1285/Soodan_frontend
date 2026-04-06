// lib/config/di/injection_container.dart
import 'package:dio/dio.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import 'package:get_it/get_it.dart';
import 'package:flutter_soodan_app/core/network/dio_client.dart';
import '../../features/auth/domain/repositories/auth_repository.dart';
import '../../features/auth/data/respositories/auth_repositoriy_impl.dart';
import '../../features/auth/data/datasources/auth_remote_data_source.dart';
import '../../features/auth/presentation/blocs/auth_bloc.dart';
import '../../core/network/interceptors/auth.dart';

final sl = GetIt.instance;

Future<void> initDependencies() async {
  // External
  const storage = FlutterSecureStorage();
  sl.registerLazySingleton(() => storage);
  
  // Core
  sl.registerLazySingleton<DioClient>(() => DioClient(
    dio: Dio()..interceptors.add(AuthInterceptor(sl()))
  ));

  // External
  await _initExternal();
  
  // Features
  _initAuth(); // Llamamos a la configuración de Auth
}

void _initAuth() {
  // 1. Data Source - Ahora le pasamos el storage explícitamente
  sl.registerLazySingleton(() => AuthRemoteDataSource(sl<DioClient>(), sl<FlutterSecureStorage>()));

  // 2. Repository
  sl.registerLazySingleton<AuthRepository>(
    () => AuthRepositoryImpl(sl<AuthRemoteDataSource>())
  );

  // 3. BLoC
  sl.registerFactory(() => AuthBloc(sl<AuthRepository>()));
}

Future<void> _initExternal() async {
  // Aquí inicializas cosas externas, por ejemplo:
  // final sharedPreferences = await SharedPreferences.getInstance();
  // sl.registerLazySingleton(() => sharedPreferences);
}
