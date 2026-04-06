import 'package:flutter_bloc/flutter_bloc.dart';
import '../../../../core/errors/failures.dart';
import '../../domain/entities/user_entity.dart';
import '../../domain/usecases/login_usecase.dart';

part 'auth_event.dart';
part 'auth_state.dart';

class AuthBloc extends Bloc<AuthEvent, AuthState> {
  final LoginUseCase loginUseCase;

  AuthBloc({required this.loginUseCase}) : super(const AuthInitial()) {
    on<LoginSubmitted>(_onLoginSubmitted);
    on<LogoutRequested>(_onLogoutRequested);
  }

  Future<void> _onLoginSubmitted(
    LoginSubmitted event,
    Emitter<AuthState> emit,
  ) async {
    emit(const AuthLoading());

    final result = await loginUseCase(event.email, event.password);

    result.fold(
      (failure) => emit(AuthFailureState(
        message: failure.message,
        failureType: _mapFailure(failure),
      )),
      (user) => emit(AuthAuthenticated(user)),
    );
  }

  Future<void> _onLogoutRequested(
    LogoutRequested event,
    Emitter<AuthState> emit,
  ) async {
    // TODO: llamar logoutUseCase cuando esté implementado
    emit(const AuthUnauthenticated());
  }

  AuthFailureType _mapFailure(Failure failure) => switch (failure) {
        UserNotVerifiedFailure() => AuthFailureType.notVerified,
        AuthFailure() => AuthFailureType.credentials,
        ValidationFailure() => AuthFailureType.validation,
        NetworkFailure() => AuthFailureType.network,
        _ => AuthFailureType.server,
      };
}