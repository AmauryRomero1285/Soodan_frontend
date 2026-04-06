// lib/features/auth/presentation/blocs/auth_bloc.dart
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:flutter_soodan_app/features/auth/domain/entities/user_entity.dart';
import 'package:flutter_soodan_app/features/auth/domain/repositories/auth_repository.dart';

abstract class AuthState {}
class AuthInitial extends AuthState {}
class AuthLoading extends AuthState {}
class AuthAuthenticated extends AuthState {
  final UserEntity user;
  AuthAuthenticated(this.user);
}
class AuthError extends AuthState {
  final String message;
  AuthError(this.message);
}

// Eventos
abstract class AuthEvent {}
class LoginSubmitted extends AuthEvent {
  final String email;
  final String password;
  LoginSubmitted(this.email, this.password);
}

class AuthBloc extends Bloc<AuthEvent, AuthState> {
  final AuthRepository repository;

  AuthBloc(this.repository) : super(AuthInitial()) {
    on<LoginSubmitted>((event, emit) async {
      emit(AuthLoading());
      try {
        final user = await repository.login(event.email, event.password);
        emit(AuthAuthenticated(user));
      } catch (e) {
        emit(AuthError(e.toString()));
      }
    });
  }
}