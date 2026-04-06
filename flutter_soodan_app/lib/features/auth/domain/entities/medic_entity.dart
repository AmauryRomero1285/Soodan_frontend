class MedicEntity {
  final String specialty;
  final String licenseNumber;
  final double doctorValue;
  final String? bio;
  final double consultationPrice;

  MedicEntity({
    required this.specialty, 
    required this.licenseNumber, 
    this.doctorValue = 5.0, 
    this.bio, 
    required this.consultationPrice
  });
}