import 'package:dio/dio.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import '../../../../core/errors/exceptions.dart';
import '../../../../core/network/dio_client.dart';
import '../models/auth_response_model.dart';
import '../models/user_model.dart';

abstract class AuthRemoteDataSource {
  Future<UserModel> login(String email, String password);
  Future<void> logout();
}

class AuthRemoteDataSourceImpl implements AuthRemoteDataSource {
  final DioClient _dioClient;
  final FlutterSecureStorage _storage;

  static const _tokenKey = 'jwt_token';

  const AuthRemoteDataSourceImpl(this._dioClient, this._storage);

  @override
  Future<UserModel> login(String email, String password) async {
    try {
      final response = await _dioClient.post(
        '/api/v1/auth/login',
        data: {'email': email, 'password': password},
      );

      final json = response.data as Map<String, dynamic>;
      final authResponse = AuthResponseModel.fromJson(json);

      await _storage.write(key: _tokenKey, value: authResponse.accessToken);

      return authResponse.user;
    } on DioException catch (e) {
      throw _mapDioException(e);
    }
  }

  @override
  Future<void> logout() async {
    await _storage.delete(key: _tokenKey);
  }

  AppException _mapDioException(DioException e) {
    final status = e.response?.statusCode;
    final data = e.response?.data;

    // Extraer mensaje de FastAPI si viene en 'detail'
    String? detail;
    if (data is Map<String, dynamic>) {
      final raw = data['detail'];
      if (raw is String) {
        detail = raw;
      } else if (raw is List && raw.isNotEmpty) {
        // Error 422 de Pydantic: lista de ValidationError
        detail = raw.first?['msg']?.toString();
      }
    }

    return switch (status) {
      401 => const UnauthorizedException(),
      403 => detail == 'USER_NOT_VERIFIED'
          ? const UserNotVerifiedException()
          : UnauthorizedException(detail ?? 'Acceso denegado.'),
      422 => ValidationException(detail ?? 'Datos inválidos. Revisa los campos.'),
      404 => const NotFoundException(),
      500 || 502 || 503 => const ServerException(),
      _ => _mapConnectionError(e),
    };
  }

  AppException _mapConnectionError(DioException e) {
    return switch (e.type) {
      DioExceptionType.connectionTimeout ||
      DioExceptionType.sendTimeout ||
      DioExceptionType.receiveTimeout =>
        const NetworkException('Tiempo de espera agotado. Verifica tu red.'),
      DioExceptionType.connectionError =>
        const NetworkException(),
      _ => const ServerException('Ocurrió un error inesperado.'),
    };
  }
}