import 'package:dartz/dartz.dart';
import '../../../../core/errors/exceptions.dart';
import '../../../../core/errors/failures.dart';
import '../../domain/entities/user_entity.dart';
import '../../domain/repositories/auth_repository.dart';
import '../datasources/auth_remote_data_source.dart';

class AuthRepositoryImpl implements AuthRepository {
  final AuthRemoteDataSource remoteDataSource;

  const AuthRepositoryImpl(this.remoteDataSource);

  @override
  Future<Either<Failure, UserEntity>> login(
    String email,
    String password,
  ) async {
    try {
      final user = await remoteDataSource.login(email, password);
      return Right(user);
    } on UserNotVerifiedException catch (e) {
      return Left(UserNotVerifiedFailure(e.message));
    } on UnauthorizedException catch (e) {
      return Left(AuthFailure(e.message));
    } on ValidationException catch (e) {
      return Left(ValidationFailure(e.message));
    } on NetworkException catch (e) {
      return Left(NetworkFailure(e.message));
    } on ServerException catch (e) {
      return Left(ServerFailure(e.message));
    }
  }

  @override
  Future<Either<Failure, void>> register(Map<String, dynamic> userData) {
    // TODO: implement register
    throw UnimplementedError();
  }

  @override
  Future<Either<Failure, void>> verifyAccount(String email, String code) {
    // TODO: implement verifyAccount
    throw UnimplementedError();
  }

  @override
  Future<Either<Failure, void>> resetPassword(
    String email,
    String code,
    String newPassword,
  ) {
    // TODO: implement resetPassword
    throw UnimplementedError();
  }
}