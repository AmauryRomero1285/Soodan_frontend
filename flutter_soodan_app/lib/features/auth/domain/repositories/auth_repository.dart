// lib/features/auth/domain/repositories/auth_repository.dart
import '../entities/user_entity.dart';

abstract class AuthRepository {
  Future<UserEntity> login(String email, String password);
  Future<void> register(Map<String, dynamic> userData);
  Future<void> verifyAccount(String email, String code);
  Future<void> resetPassword(String email, String code, String newPassword);
}