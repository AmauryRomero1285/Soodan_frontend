import 'package:go_router/go_router.dart';
import 'package:flutter_soodan_app/config/routes/app_routes.dart';
import 'package:flutter_soodan_app/features/pages.examples/dashboard.dart';


class AppRouter {
  static final GoRouter router = GoRouter(
    initialLocation: AppRoutes.splash,
    routes: [
      GoRoute(
        path: AppRoutes.splash,
        name: AppRoutes.splash,
        builder: (context, state) => const DashboardScreen(),
      ),
       
      GoRoute(
        path: AppRoutes.home,
        name: AppRoutes.home,
        builder: (context,state)=> const DashboardScreen(),
      ), 
    ],
  );
}

