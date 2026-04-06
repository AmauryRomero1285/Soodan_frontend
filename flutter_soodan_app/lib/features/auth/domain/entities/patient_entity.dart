class PatientEntity {
  final int id;
  final DateTime? birthDate;
  final String? bloodType;
  final String? allergies;
  final double? height;
  final double? weight;

  const PatientEntity({
    required this.id,
    this.birthDate,
    this.bloodType,
    this.allergies,
    this.height,
    this.weight,
  });
}