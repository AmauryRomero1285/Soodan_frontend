import 'package:flutter/material.dart';

import 'app_colors.dart';
import 'app_text_styles.dart';

class AppTheme {
  static ThemeData lightTheme=ThemeData(
    primaryColor: AppColors.primary,
    colorScheme: const ColorScheme.light(
      primary: AppColors.primary,
      secondary: AppColors.secondary
    ),
    textTheme: TextTheme(
      //Titles
      titleLarge: AppTextStyles.titleLarge,
      //body
      bodyLarge:AppTextStyles.titleLarge,
      bodyMedium: AppTextStyles.bodyMedium ,
      headlineMedium: AppTextStyles.headlineMedium,
    ),
  );
}