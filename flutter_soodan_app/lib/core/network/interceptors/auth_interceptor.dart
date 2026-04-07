// interceptors/auth.dart
import 'package:dio/dio.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

class AuthInterceptor extends Interceptor {
  final FlutterSecureStorage _storage;

  AuthInterceptor(this._storage);

  @override
  Future<void> onRequest(
    RequestOptions options, 
    RequestInterceptorHandler handler
  ) async {
    // 1. No añadir token si es la ruta de login o registro
    // Esto evita conflictos con el flujo de obtención de un nuevo token
    if (options.path.contains('/auth/login') || options.path.contains('/auth/register')) {
      return handler.next(options);
    }

    // 2. Intentar leer el token de la persistencia segura
    final token = await _storage.read(key: 'jwt_token');
    
    if (token != null && token.isNotEmpty) {
      options.headers['Authorization'] = 'Bearer $token';
    }

    // 3. Continuar con la petición
    return handler.next(options);
  }

  @override
  void onError(DioException err, ErrorInterceptorHandler handler) {
    // 4. Tip Pro: Si recibimos un 401 (Unauthorized) en cualquier parte de la app,
    // significa que el token expiró. Aquí podrías disparar un evento de Logout global.
    if (err.response?.statusCode == 401) {
      // Opcional: Notificar al AuthBloc para redirigir al Login
      print("Token expirado o inválido. Redirigiendo...");
    }
    return handler.next(err);
  }
}