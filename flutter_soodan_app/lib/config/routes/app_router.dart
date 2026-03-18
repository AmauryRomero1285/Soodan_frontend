import 'package:go_router/go_router.dart';
import 'package:flutter_soodan_app/config/routes/app_routes.dart';
import 'package:flutter_soodan_app/features/auth/presentation/pages/splash_page.dart'; // Ajusta la ruta según tu carpetas


class AppRouter {
  static final GoRouter router = GoRouter(
    initialLocation: AppRoutes.splash,
    routes: [
      GoRoute(
        path: AppRoutes.splash,
        name: AppRoutes.splash,
        builder: (context, state) => const SplashPage(),
      ),
      /* 
      GoRoute(
        path: AppRoutes.login,
        name: AppRoutes.login,
      ), 
      */
    ],
  );
}

