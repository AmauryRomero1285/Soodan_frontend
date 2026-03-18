import 'package:flutter/material.dart';
import 'package:flutter_soodan_app/core/theme/app_colors.dart';
import 'package:flutter_soodan_app/core/theme/app_text_styles.dart';

class SplashPage extends StatelessWidget {
  const SplashPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const SizedBox(height: 20),
            Text('bienvenido a Soodan', style:AppTextStyles.titleLarge),
            const CircularProgressIndicator(),
            const SizedBox(height: 20),
            Text(
              'Cargando...',
              style: Theme.of(context).textTheme.titleMedium,
            ),
          ],
        ),
      ),
    );
  }
}
