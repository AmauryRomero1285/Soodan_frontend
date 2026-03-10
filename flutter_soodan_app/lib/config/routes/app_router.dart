import 'package:flutter/material.dart';

class AppRouter {
  static Route<dynamic> generateRoute(RouteSettings settings) {
    switch (settings.name) {
      case '/':
        return MaterialPageRoute(builder: (_) => const Scaffold(body: Center(child: Text("Home"))));
      // Aquí añadirás más casos para tus "features"
      default:
        return MaterialPageRoute(
          builder: (_) => Scaffold(
            body: Center(child: Text('No existe ruta para ${settings.name}')),
          ),
        );
    }
  }
}
