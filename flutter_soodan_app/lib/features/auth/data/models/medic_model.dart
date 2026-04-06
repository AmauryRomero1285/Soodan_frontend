// lib/features/auth/data/models/medic_model.dart
import '../../domain/entities/medic_entity.dart';

class MedicModel extends MedicEntity {
  MedicModel({
    required String specialty,
    required String licenseNumber,
    double doctorValue = 5.0,
    String? bio,
    required double consultationPrice,
  }) : super(
          specialty: specialty,
          licenseNumber: licenseNumber,
          doctorValue: doctorValue,
          bio: bio,
          consultationPrice: consultationPrice,
        );

  factory MedicModel.fromJson(Map<String, dynamic> json) {
    return MedicModel(
      specialty: json['specialty'],
      licenseNumber: json['license_number'],
      doctorValue: (json['doctor_value'] as num).toDouble(),
      bio: json['bio'],
      consultationPrice: (json['consultation_price'] as num).toDouble(),
    );
  }
}