📚 FastAPI Library Management API
Una API REST construida con FastAPI/Swagger y Sqlite para gestionar usuarios, libros y relaciones entre ellos. Incluye autenticación básica, filtrado de resultados y una arquitectura organizada por controladores, modelos, repositorios y esquemas.

~ Características
CRUD completo para usuarios y libros

- Relación muchos-a-muchos entre usuarios y libros

- Filtros por categoría y estado (is_active) con query parameters

- Autenticación HTTP Basic para operaciones protegidas

- Datos en formato JSON para autores, categorías e imágenes

- Separación clara de responsabilidades (repositorios, controladores, routers, etc.)


~ Estructura del proyecto

```bash 
app/
├── auth/               # Lógica de autenticación
├── controllers/        # Lógica de negocio
├── db/                 # Conexión y base de datos SQLite
├── models/             # Modelos SQLModel
├── repositories/       # Funciones de acceso a datos
├── routers/            # Rutas agrupadas por recurso
├── schemas/            # Esquemas Pydantic para entrada/salida
├── utils/              # Utilidades, seeders, errores personalizados
└── main.py             # Punto de entrada principal 
```

