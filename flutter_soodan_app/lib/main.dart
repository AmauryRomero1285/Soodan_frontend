import 'package:flutter/material.dart';
import 'package:flutter_soodan_app/config/di/injection_container.dart';
import 'package:flutter_soodan_app/config/routes/app_router.dart';
import 'package:flutter_soodan_app/core/theme/app_theme.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  //inicializar dependencias
  await initDependencies();

  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp.router(
      title: 'Soodan',
      theme: AppTheme.lightTheme,
      routerConfig: AppRouter.router,
      debugShowCheckedModeBanner: false,
    );
  }
}
