// app_routes.dart
class AppRoutes {
  AppRoutes._();

  // ── Paths ────────────────────────────────────────────
  static const String login          = '/login';
  static const String register       = '/register';
  static const String verifyAccount  = '/verify-account';
  static const String forgotPassword = '/forgot-password';
  static const String resetPassword  = '/reset-password';
  static const String home           = '/home';

  // ── Helpers con query params ─────────────────────────
  static String verifyAccountWithEmail(String email) =>
      '$verifyAccount?email=${Uri.encodeComponent(email)}';

  static String resetPasswordWithEmail(String email) =>
      '$resetPassword?email=${Uri.encodeComponent(email)}';
}