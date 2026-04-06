import 'package:dio/dio.dart';
import 'package:flutter_soodan_app/config/app_config.dart';

class DioClient {
  late final Dio dio;

  // Si pasas un Dio por parámetro (para pruebas), lo usa. 
  // Si no, crea uno nuevo con la configuración base.
  DioClient({Dio? existingDio, required Dio dio}) {
    dio = existingDio ?? Dio(BaseOptions(
      baseUrl: AppConfig.environment,
      connectTimeout: const Duration(seconds: 30),
      receiveTimeout: const Duration(seconds: 30),
      headers: {'Content-Type': 'application/json'},
    ));

    dio.interceptors.add(LogInterceptor(
      responseBody: true,
      requestBody: true,
    ));
  }

  // IMPORTANTE: El método debe ser async y retornar el resultado de dio.post
  Future<Response> post(String path, {required dynamic data}) async {
    try {
      final response = await dio.post(path, data: data);
      return response;
    } on DioException {
      rethrow; // Re-lanzamos para que el DataSource lo capture
    }
  }
}