import 'user_model.dart';

/// Mapea la respuesta completa del endpoint POST /api/v1/auth/login
/// Estructura esperada del backend FastAPI:
/// {
///   "access_token": "eyJ...",
///   "token_type": "bearer",
///   "user": { "profile": {...}, "role": "medic", "role_data": {...} }
/// }
class AuthResponseModel {
  final String accessToken;
  final String tokenType;
  final UserModel user;

  const AuthResponseModel({
    required this.accessToken,
    required this.tokenType,
    required this.user,
  });

  factory AuthResponseModel.fromJson(Map<String, dynamic> json) {
    return AuthResponseModel(
      accessToken: json['access_token'] as String,
      tokenType: json['token_type'] as String? ?? 'bearer',
      user: UserModel.fromJson(json['user'] as Map<String, dynamic>),
    );
  }
}