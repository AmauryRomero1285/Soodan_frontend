text
```
app/
├── core/
│   ├── config.py
│   ├── security.py
│   └── dependencies.py
├── models/
│   ├── __init__.py
│   ├── base.py
│   ├── profile.py
│   ├── medic.py
│   ├── patient.py
│   └── session.py          # UserSession persistente
├── schemas/
│   ├── __init__.py
│   ├── auth.py
│   ├── profile.py
│   ├── medic.py
│   └── patient.py
├── api/v1/
│   └── auth.py
├── database/
│   └── connection.py
└── main.py
```