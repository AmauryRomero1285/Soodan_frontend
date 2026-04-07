// lib/core/constants/app_constants.dart

abstract class AppConstants {
  // Storage keys — una sola fuente de verdad, 
  // referenciada desde AuthInterceptor y DataSource
  static const String jwtTokenKey      = 'jwt_token';
  static const String userRoleKey       = 'user_role';

  // Timeouts
  static const Duration connectTimeout  = Duration(seconds: 30);
  static const Duration receiveTimeout  = Duration(seconds: 30);

  // Paginación (para cuando implementes listas)
  static const int defaultPageSize      = 20;

  // App
  static const String appName           = 'Soodan';
}