/// Mapea exactamente la respuesta de POST /api/v1/auth/login:
/// {
///   "access_token": "eyJ...",
///   "token_type": "bearer",
///   "user": {
///     "id": 11,
///     "email": "medic@soodan.com",
///     "name": "Alan",
///     "lastname": "Turing",
///     "role": "medic"
///   }
/// }
class AuthResponseModel {
  final String accessToken;
  final String tokenType;
  final AuthUserPayload user;

  const AuthResponseModel({
    required this.accessToken,
    required this.tokenType,
    required this.user,
  });

  factory AuthResponseModel.fromJson(Map<String, dynamic> json) {
    return AuthResponseModel(
      accessToken: json['access_token'] as String,
      tokenType: json['token_type'] as String? ?? 'bearer',
      user: AuthUserPayload.fromJson(json['user'] as Map<String, dynamic>),
    );
  }
}

/// Payload mínimo que devuelve el login.
/// No confundir con UserModel completo — ese viene del endpoint de perfil.
class AuthUserPayload {
  final int id;
  final String email;
  final String name;
  final String lastname;
  final String role;

  const AuthUserPayload({
    required this.id,
    required this.email,
    required this.name,
    required this.lastname,
    required this.role,
  });

  factory AuthUserPayload.fromJson(Map<String, dynamic> json) {
    return AuthUserPayload(
      id: json['id'] as int,
      email: json['email'] as String,
      name: json['name'] as String,
      lastname: json['lastname'] as String,
      role: json['role'] as String,
    );
  }
}