// lib/core/constants/api_endpoints.dart

abstract class ApiEndpoints {
  // ── Auth ────────────────────────────────
  static const String login           = '/api/v1/auth/login';
  static const String register        = '/api/v1/auth/register';
  static const String verifyAccount   = '/api/v1/auth/verify';
  static const String forgotPassword  = '/api/v1/auth/forgot-password';
  static const String resetPassword   = '/api/v1/auth/reset-password';

  // ── User / Profile ───────────────────────
  static const String me              = '/api/v1/users/me';

  // ── Medic ────────────────────────────────
  static const String medics          = '/api/v1/medics';
  static String medicById(int id)     => '/api/v1/medics/$id';

  // ── Patient ──────────────────────────────
  static const String patients        = '/api/v1/patients';
  static String patientById(int id)   => '/api/v1/patients/$id';
}