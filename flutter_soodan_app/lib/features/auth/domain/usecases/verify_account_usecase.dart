import '../repositories/auth_repository.dart';

class VerifyAccountUseCase {
  final AuthRepository repository;
  VerifyAccountUseCase(this.repository);

  Future<void> call(String email, String code) {
    return repository.verifyAccount(email, code);
  }
}