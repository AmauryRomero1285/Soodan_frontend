// lib/features/auth/domain/entities/user_entity.dart
enum UserRole { admin, medic, patient }

class ProfileEntity {
  final int id; 
  final String email;
  final String name;
  final String lastname;
  final String? avatarUrl;
  final String? phoneNumber;
  final UserRole role;
  final DateTime? createdAt;
  final bool isVerified;

  ProfileEntity({
    required this.id,
    required this.email,
    required this.name,
    required this.lastname,
    this.avatarUrl,
    this.phoneNumber,
    required this.role,
    this.createdAt,
    this.isVerified = false,
  });
  String get fullName => '$name $lastname';
}

class UserEntity {
  final ProfileEntity profile;
  final UserRole role; 
  final dynamic roleData; // MedicEntity | PatientEntity | Null

  UserEntity({
    required this.profile, 
    required this.role, 
    this.roleData,
  });
}
