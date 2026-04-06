import 'package:dartz/dartz.dart';
import '../../../../core/errors/failures.dart';
import '../entities/user_entity.dart';

abstract class AuthRepository {
  Future<Either<Failure, UserEntity>> login(String email, String password);
  Future<Either<Failure, void>> register(Map<String, dynamic> userData);
  Future<Either<Failure, void>> verifyAccount(String email, String code);
  Future<Either<Failure, void>> resetPassword(
    String email,
    String code,
    String newPassword,
  );
}