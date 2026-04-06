//lib/features/auth/data/respositories/auth_repositoriy_impl.dart
import '../../domain/entities/user_entity.dart';
import '../../domain/repositories/auth_repository.dart';
import '../datasources/auth_remote_data_source.dart';

class AuthRepositoryImpl implements AuthRepository {
  final AuthRemoteDataSource remoteDataSource;

  AuthRepositoryImpl(this.remoteDataSource);

  @override
  Future<UserEntity> login(String email, String password) async {
    return await remoteDataSource.login(email, password);
  }
  
  @override
  Future<void> register(Map<String, dynamic> userData) {
    // TODO: implement register
    throw UnimplementedError();
  }
  
  @override
  Future<void> resetPassword(String email, String code, String newPassword) {
    // TODO: implement resetPassword
    throw UnimplementedError();
  }
  
  @override
  Future<void> verifyAccount(String email, String code) {
    // TODO: implement verifyAccount
    throw UnimplementedError();
  }

  // Implementa los demás overrides (register, verify, reset)...
}