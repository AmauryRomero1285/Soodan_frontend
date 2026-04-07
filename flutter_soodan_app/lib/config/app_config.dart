abstract class AppConfig {
  // URL base de la API — inyectada en build time
  // Uso: flutter run --dart-define=API_URL=https://api.soodan.com
  static const String baseUrl = String.fromEnvironment(
    'API_URL',
    defaultValue: 'http://localhost:8000', // Android emulator → localhost
  );

  // Nombre del entorno — para logs y flags condicionales
  // Uso: flutter run --dart-define=ENVIRONMENT=prod
  static const String environment = String.fromEnvironment(
    'ENVIRONMENT',
    defaultValue: 'dev',
  );

  // Flags derivados — sin lógica en el DioClient
  static bool get isProduction => environment == 'prod';
  static bool get isDevelopment => environment == 'dev';
}