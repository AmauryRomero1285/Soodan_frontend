import '../../domain/entities/patient_entity.dart';

class PatientModel extends PatientEntity {
  const PatientModel({
    required super.id,
    super.birthDate,
    super.bloodType,
    super.allergies,
    super.height,
    super.weight,
  });

  factory PatientModel.fromJson(Map<String, dynamic> json) {
    return PatientModel(
      id: json['id'] as int,
      birthDate: json['birth_date'] != null
          ? DateTime.tryParse(json['birth_date'] as String)
          : null,
      bloodType: json['blood_type'] as String?,
      allergies: json['allergies'] as String?,
      height: json['height'] != null
          ? double.tryParse(json['height'].toString())
          : null,
      weight: json['weight'] != null
          ? double.tryParse(json['weight'].toString())
          : null,
    );
  }

  Map<String, dynamic> toJson() => {
        'id': id,
        'birth_date': birthDate?.toIso8601String().split('T').first,
        'blood_type': bloodType,       // null explícito para Pydantic
        'allergies': allergies,
        'height': height,
        'weight': weight,
      };
}