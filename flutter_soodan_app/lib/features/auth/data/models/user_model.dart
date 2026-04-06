// lib/features/auth/data/models/user_model.dart
import '../../domain/entities/user_entity.dart';

class UserModel extends UserEntity {
  UserModel({
    required ProfileModel profile,
    required UserRole role,
    dynamic roleData,
  }) : super(profile: profile, role: role, roleData: roleData);

  factory UserModel.fromJson(Map<String, dynamic> json) {
    // Mapeo del string del backend al enum de Dart
    final roleStr = json['role']?.toString().toLowerCase();
    final role = UserRole.values.firstWhere(
      (e) => e.name == roleStr,
      orElse: () => UserRole.patient,
    );

    return UserModel(
      profile: ProfileModel.fromJson(json['profile'] ?? json), // Depende de si el JSON viene anidado o plano
      role: role,
      roleData: json['role_data'], // Datos específicos de Medic/Patient si existen
    );
  }
}

class ProfileModel extends ProfileEntity {
  ProfileModel({
    required int id,
    required String email,
    required String name,
    required String lastname,
    String? avatarUrl,
    String? phoneNumber,
    required UserRole role,
    bool isVerified = false,
  }) : super(
          id: id,
          email: email,
          name: name,
          lastname: lastname,
          avatarUrl: avatarUrl,
          phoneNumber: phoneNumber,
          role: role,
          isVerified: isVerified,
        );

  factory ProfileModel.fromJson(Map<String, dynamic> json) {
    return ProfileModel(
      id: json['id'],
      email: json['email'],
      name: json['name'],
      lastname: json['lastname'],
      avatarUrl: json['avatar_url'],
      phoneNumber: json['phone_number'],
      role: UserRole.values.firstWhere(
        (e) => e.name == json['role'],
        orElse: () => UserRole.patient,
      ),
      // Convertimos el 1/0 de SQLAlchemy a bool
      isVerified: json['is_verified'] == 1,
    );
  }
}
