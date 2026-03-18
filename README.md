# Soodan – Mobile Frontend (Flutter)

![Flutter](https://img.shields.io/badge/Flutter-02569B?logo=flutter&logoColor=white)
![Dart](https://img.shields.io/badge/Dart-0175C2?logo=dart&logoColor=white)
![Version](https://img.shields.io/badge/version-1.0.0-blue?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)

Soodan is a comprehensive digital health platform designed to facilitate interaction between patients and medics, improve treatment tracking, and promote self-care in a secure and accessible way.

## Key Features

- **Secure Authentication:** Multi-role support (Patients, Doctors, and Admins).
- **Medical Agenda:** Scheduling, reminders, and cancellations with Push Notifications.
- **Telemedicine:** Video consultations via WebRTC/Agora and real-time chat.
- **Health Tracking:** Daily monitoring of vital signs, symptoms, and lab results.
- **UX/UI:** Automatic Dark/Light mode and multi-language support (ES/EN).
- **Accessibility:** Responsive design following basic accessibility standards.

## Tech Stack

- **State Management:** [Bloc/Cubit](https://pub.dev) (Predictable state management).
- **Dependency Injection:** [GetIt](https://pub.dev).
- **Navigation:** [GoRouter](https://pub.dev) / [AutoRouter].
- **Network:** [Dio](https://pub.dev) with interceptors for JWT handling.
- **Local Storage:** [Hive](https://pub.dev) or [Isar] for caching.
- **Architecture:** Clean Architecture (Data, Domain, Presentation).

## Folder Structure (Temporary)

```text
lib/
├── main.dart
│
├── config/
│   ├── app_config.dart
│   ├── routes/
│   │   ├── app_router.dart
│   │   └── app_routes.dart
│   ├── di/                   # Dependency Injection
│       └── injection_container.dart
│
├── core/                     # Items that do NOT belong to any specific feature
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
│   │   │   ├── entities/         # business models
│   │   │   ├── repositories/     # abstract interface
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
│   │   └── (same structure)
│   │
│   ├── profile/
│   ├── medical_record/
│   ├── chat/
│   └── videocall/
│
└── shared/
    ├── widgets/               # generics (button, card, loading, etc.)
    ├── components/            # complex (date_picker_modal, custom_app_bar, etc.)
    ├── models/                # shared models (UserRole, Gender, Country…)
    └── services/              # global services (analytics, crashlytics, permissions…)

```
