import 'package:dio/dio.dart';
import 'package:flutter/foundation.dart'; // Para kDebugMode
import '../../config/app_config.dart';
import 'interceptors/auth_interceptor.dart'; // Ajusta la ruta según tu carpeta

class DioClient {
  final Dio dio;

  DioClient({
    Dio? existingDio,
    required AuthInterceptor authInterceptor, // Inyección obligatoria
  }) : dio = existingDio ??
            Dio(
              
              BaseOptions(
                baseUrl: AppConfig.baseUrl.endsWith('/')
                    ? AppConfig.baseUrl
                    : '${AppConfig.baseUrl}/', // Asegura la barra final
                connectTimeout: const Duration(seconds: 30),
                receiveTimeout: const Duration(seconds: 30),
                headers: {'Content-Type': 'application/json'},
              ),
            ) {
    
    // 1. Agregar Interceptor de Autenticación
    dio.interceptors.add(authInterceptor);

    // 2. Agregar Interceptor de Logs (Solo en Desarrollo)
    if (kDebugMode) {
      dio.interceptors.add(LogInterceptor(
        requestHeader: true,
        requestBody: true,
        responseHeader: false,
        responseBody: true,
        error: true,
      ));
    }
  }

  // Métodos Wrapper (Post, Get, Put, Delete)
  // Tip: No necesitas el try-catch con rethrow si no vas a transformar el error aquí.
  // El rethrow es redundante, pero lo mantengo para seguir tu estilo actual.
Future<Response> post(String path, {required dynamic data}) async {
  try {
    // Si el path viene con "/", se lo quitamos para que use la baseUrl
    final cleanPath = path.startsWith('/') ? path.substring(1) : path;
    return await dio.post(cleanPath, data: data);
  } on DioException {
    rethrow;
  }
}

  Future<Response> get(String path, {Map<String, dynamic>? queryParams}) async {
    try {
      return await dio.get(path, queryParameters: queryParams);
    } on DioException {
      rethrow;
    }
  }

  Future<Response> put(String path, {required dynamic data}) async {
    try {
      return await dio.put(path, data: data);
    } on DioException {
      rethrow;
    }
  }

  Future<Response> delete(String path) async {
    try {
      return await dio.delete(path);
    } on DioException {
      rethrow;
    }
  }
}