# Soodan – Frontend Móvil (Flutter)

Aplicación móvil para pacientes y profesionales de la salud desarrollada con **Flutter**.

Soodan es una plataforma integral de salud digital diseñada para facilitar la interacción entre pacientes y médicos, mejorar el seguimiento de tratamientos y promover el autocuidado de manera segura y accesible.

## ✨ Características principales

- Autenticación segura (pacientes, médicos y administradores)
- Perfil de usuario completo (paciente y profesional de salud)
- Agenda y citas médicas (programación, recordatorios, cancelaciones)
- Historial clínico accesible y controlado
- Registro de signos vitales y síntomas diarios
- Recordatorios de medicamentos y tomas (con notificaciones push)
- Videoconsultas (integración con WebRTC / Agora / similar)
- Chat en tiempo real con el médico asignado
- Resultados de laboratorio e imágenes diagnósticas
- Modo oscuro / claro automático
- Soporte multilenguaje (español + inglés inicial)
- Diseño responsivo y accesible (cumpliendo estándares básicos de accesibilidad)

## 📂 Estructura de carpetas (Temporal)

```text
lib/
├── core/               # Configuraciones globales, temas, constantes y helpers.
├── features/           # Módulos funcionales de la aplicación:
│   ├── auth/           # Gestión de autenticación y sesiones.
│   ├── home/           # Pantalla principal y dashboards.
│   ├── appointments/   # Gestión de citas médicas.
│   ├── profile/        # Información y ajustes del usuario.
│   ├── medical_record/ # Historial y expedientes médicos.
│   ├── chat/           # Mensajería interna.
│   ├── videocall/      # Funcionalidad de telemedicina.
│   └── ...
│
├── shared/             # Código compartido entre múltiples features:
│   ├── widgets/        # Widgets atómicos y reutilizables.
│   ├── components/     # Piezas de UI más complejas (ej. modales, layouts).
│   └── extensions/     # Extensiones de Dart/Flutter.
│   
├── config/             # Rutas, inyección de dependencias y variables de entorno.
├── generated/          # Código autogenerado (Freezed, JSON Serializable, etc.).
└── main.dart           # Punto de entrada de la aplicación.
```


