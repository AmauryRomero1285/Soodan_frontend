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
├── main.dart
│
├── config/                
│   ├── app_config.dart
│   ├── routes/
│   │   ├── app_router.dart           
│   │   └── app_routes.dart
│   ├── di/                   # Inyección de dependencias
│       └── injection_container.dart
│
├── core/                     # Cosas que NO pertenecen a ninguna feature específica
│   ├── constants/
│   ├── errors/
│   ├── network/              # dio, interceptors, connectivity
│   ├── theme/
│   │   ├── app_colors.dart
│   │   ├── app_text_styles.dart
│   │   └── app_theme.dart
│   ├── usecases/             # usecases
│   └── utils/
│       ├── extensions/
│       └── helpers.dart
│
├── features/                 
│   ├── auth/
│   │   ├── data/
│   │   │   ├── datasources/      
│   │   │   ├── models/           
│   │   │   └── repositories/
│   │   ├── domain/
│   │   │   ├── entities/         # modelos de negocio
│   │   │   ├── repositories/     # interfaz abstracta
│   │   │   └── usecases/
│   │   └──  presentation/
│   │       ├── blocs /
│   │       ├── pages/            
│   │       ├── widgets/
│   │       └── login/ forgot_password/ register/ etc.
│   │   
│   │
│   ├── home/
│   │   ├── data/
│   │   ├── domain/
│   │   └── presentation/
│   │
│   ├── appointments/
│   │   └── (igual estructura)
│   │
│   ├── profile/
│   ├── medical_record/
│   ├── chat/
│   └── videocall/
│
└── shared/
    ├── widgets/               # genéricos (button, card, loading, etc.)
    ├── components/            # complejos (date_picker_modal, custom_app_bar, etc.)
    ├── models/                # modelos compartidos (UserRole, Gender, Country…)
    └── services/              # servicios globales (analytics, crashlytics, permissions…)
```


