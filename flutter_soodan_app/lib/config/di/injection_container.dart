import 'package:get_it/get_it.dart';
import 'package:flutter_soodan_app/core/network/dio_client.dart';

final sl = GetIt.instance;

Future<void> initDependencies() async {
  // Core
  sl.registerLazySingleton<DioClient>(() => DioClient());
  
  // External
  await _initExternal();
  
  // Features (irás agregando después)
  // await _initAuth();
}

Future <void> _initExternal() async {
  //shared preferences, secure storage, etc
  //ex:
  //final prefs = await SharedPreferences.getInstance();
  //sl.registerLazySingleton(()=>prefs);
}