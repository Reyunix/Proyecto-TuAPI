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

~ Autenticación
Algunas rutas estan protegidas por credenciales así que para tener acceso deberás:

1. Crear un archivo .env
2. Configurar las variables USERNAME="usuario" y PASSWORD="contraseña"

~ Instalación

1. Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/nombre-repo.git
cd nombre-repo
```
2. Crear y activar el entorno virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instalar las dependencias
```bash
pip install -r requirements.txt
```

4. Arrancar FastAPI
```bash
fastapi dev app/main.py
```

~ Enpoints Principales

- GET /users → Lista de usuarios (con filtro ?is_active=true)

- POST /users → Crear usuario

- GET /books → Lista de libros (con filtro ?category=Fantasy)

- POST /books → Crear libro (requiere autenticación)

- POST /user/{user_id}/books/{book_id} → Asignar libro a usuario (requiere autenticación)

- DELETE /books/{book_id} → Eliminar libro (requiere autenticación)

~ Testing

Puedes testear los endpoints desde: http://localhost:8000/docs