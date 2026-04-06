part of 'auth_bloc.dart';

abstract class AuthState {
  const AuthState();
}

class AuthInitial extends AuthState {
  const AuthInitial();
}

class AuthLoading extends AuthState {
  const AuthLoading();
}

class AuthAuthenticated extends AuthState {
  final UserEntity user;
  const AuthAuthenticated(this.user);
}

class AuthUnauthenticated extends AuthState {
  const AuthUnauthenticated();
}

/// Estado de error tipado — el UI decide qué hacer según el tipo
class AuthFailureState extends AuthState {
  final String message;
  final AuthFailureType failureType;

  const AuthFailureState({
    required this.message,
    required this.failureType,
  });
}

enum AuthFailureType {
  credentials,    // 401 — credenciales incorrectas
  notVerified,    // 403 — cuenta sin verificar
  validation,     // 422 — campos inválidos
  network,        // sin conexión
  server,         // 500+
}