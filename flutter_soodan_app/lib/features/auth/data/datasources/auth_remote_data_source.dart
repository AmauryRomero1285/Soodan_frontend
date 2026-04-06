// lib/features/auth/data/datasources/auth_remote_data_source.dart
import 'package:dio/dio.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import '../../../../core/network/dio_client.dart';
import '../models/user_model.dart';

class AuthRemoteDataSource {
  final DioClient _dioClient;
  final FlutterSecureStorage _storage;

  AuthRemoteDataSource(this._dioClient, this._storage);

    Future<UserModel> login(String email, String password) async {
      try {
        // Ahora 'response' es de tipo Response automáticamente
        final response = await _dioClient.post(
          '/api/v1/auth/login',
          data: {
            'email': email,
            'password': password,
          },
        );

        // Dart ya no se quejará de .data
        final Map<String, dynamic> responseData =
            response.data as Map<String, dynamic>;

        // Guardar token (FastAPI suele devolver access_token)
        final String? token = responseData['access_token'];
        if (token != null) {
          await _storage.write(key: 'jwt_token', value: token);
        }

        return UserModel.fromJson(responseData);
      } on DioException catch (e) {
        // Manejo de errores de tu FastAPI
        if (e.response?.statusCode == 403) throw Exception("USER_NOT_VERIFIED");

        final msg =
            e.response?.data is Map ? e.response?.data['detail'] : 'Error';
        throw Exception(msg);
      }
    }
  }
