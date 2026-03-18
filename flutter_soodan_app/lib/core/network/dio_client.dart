import 'package:dio/dio.dart';
import 'package:flutter_soodan_app/config/app.config.dart';

class DioClient {
  late final Dio dio;

  DioClient(){
    dio=Dio(BaseOptions(
      baseUrl: AppConfig.apiBaseUrl,
      connectTimeout: const Duration(seconds: 30),
      receiveTimeout: const Duration(seconds: 30),
      headers: {'Content-Type':'application/json'},
    ));

    dio.interceptors.add(LogInterceptor(responseBody: true));
    
  }
}