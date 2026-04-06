part of 'auth_bloc.dart';

abstract class AuthEvent {
  const AuthEvent();
}

class LoginSubmitted extends AuthEvent {
  final String email;
  final String password;
  const LoginSubmitted(this.email, this.password);
}

class LogoutRequested extends AuthEvent {
  const LogoutRequested();
}