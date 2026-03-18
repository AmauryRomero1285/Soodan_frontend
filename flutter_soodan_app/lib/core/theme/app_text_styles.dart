import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'app_colors.dart';

class AppTextStyles {
  //titles
  static TextStyle titleLarge=GoogleFonts.kantumruyPro(
    fontSize: 22,
    fontWeight: FontWeight.bold,
    color:AppColors.primary,
  //Revisar si se puede implementar más colores sobre una misma class
  );

  //body
  static TextStyle bodyMedium=GoogleFonts.kantumruyPro(
    fontSize: 16,
    color: AppColors.primary,
  );

  //headline
  static TextStyle headlineMedium=GoogleFonts.kantumruyPro(
    fontSize: 12,
    color: AppColors.backgound
  );
}