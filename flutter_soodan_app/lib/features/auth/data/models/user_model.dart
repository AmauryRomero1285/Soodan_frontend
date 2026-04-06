import '../../domain/entities/user_entity.dart';
import 'medic_model.dart';
import 'patient_model.dart';

class UserModel extends UserEntity {
  const UserModel({
    required ProfileModel profile,
    required UserRole role,
    dynamic roleData,
  }) : super(profile: profile, role: role, roleData: roleData);

  factory UserModel.fromJson(Map<String, dynamic> json) {
    final roleStr = json['role']?.toString().toLowerCase();
    final role = UserRole.values.firstWhere(
      (e) => e.name == roleStr,
      orElse: () => UserRole.patient,
    );

    // Parsear roleData según el rol
    dynamic roleData;
    if (json['role_data'] != null) {
      roleData = switch (role) {
        UserRole.medic =>
          MedicModel.fromJson(json['role_data'] as Map<String, dynamic>),
        UserRole.patient =>
          PatientModel.fromJson(json['role_data'] as Map<String, dynamic>),
        _ => null,
      };
    }

    return UserModel(
      profile: ProfileModel.fromJson(json['profile'] ?? json),
      role: role,
      roleData: roleData,
    );
  }
}

class ProfileModel extends ProfileEntity {
  const ProfileModel({
    required super.id,
    required super.email,
    required super.name,
    required super.lastname,
    super.avatarUrl,
    super.phoneNumber,
    required super.role,
    super.createdAt,
    super.isVerified,
  });

  factory ProfileModel.fromJson(Map<String, dynamic> json) {
    final roleStr = json['role']?.toString().toLowerCase();
    return ProfileModel(
      id: json['id'] as int,
      email: json['email'] as String,
      name: json['name'] as String,
      lastname: json['lastname'] as String,
      avatarUrl: json['avatar_url'] as String?,
      phoneNumber: json['phone_number'] as String?,
      role: UserRole.values.firstWhere(
        (e) => e.name == roleStr,
        orElse: () => UserRole.patient,
      ),
      createdAt: json['created_at'] != null
          ? DateTime.tryParse(json['created_at'] as String)
          : null,
      // SQLAlchemy puede devolver 1/0 o true/false
      isVerified: switch (json['is_verified']) {
        true => true,
        1 => true,
        _ => false,
      },
    );
  }

  Map<String, dynamic> toJson() => {
        'id': id,
        'email': email,
        'name': name,
        'lastname': lastname,
        'avatar_url': avatarUrl,     // null explícito
        'phone_number': phoneNumber,
        'role': role.name,
        'created_at': createdAt?.toIso8601String(),
        'is_verified': isVerified,
      };
}