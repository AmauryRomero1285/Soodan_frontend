/// Excepción base de la app
abstract class AppException implements Exception {
  final String message;
  const AppException(this.message);

  @override
  String toString() => message;
}

class UnauthorizedException extends AppException {
  const UnauthorizedException([
    super.message = 'Correo o contraseña incorrectos.',
  ]);
}

class UserNotVerifiedException extends AppException {
  const UserNotVerifiedException([
    super.message = 'Tu cuenta aún no ha sido verificada.',
  ]);
}

class ValidationException extends AppException {
  const ValidationException(super.message);
}

class ServerException extends AppException {
  const ServerException([
    super.message = 'Error interno del servidor. Intenta más tarde.',
  ]);
}

class NetworkException extends AppException {
  const NetworkException([
    super.message = 'Sin conexión a internet. Verifica tu red.',
  ]);
}

class NotFoundException extends AppException {
  const NotFoundException([
    super.message = 'Recurso no encontrado.',
  ]);
}