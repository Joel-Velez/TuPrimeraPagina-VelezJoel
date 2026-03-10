# TuPrimeraPagina - Joel Velez

Proyecto realizado con Django para practicar CRUD, autenticación y uso de plantillas.

## Funcionalidades

- CRUD de Cargos
- CRUD de Empleados
- CRUD de Tareas
- Sistema de autenticación (login, logout, registro)
- Búsqueda en la base de datos
- Página About del alumno
- Templates con Bootstrap

## Cómo ejecutar el proyecto

1. Clonar el repositorio

    - git clone https://github.com/Joel-Velez/TuPrimeraPagina-VelezJoel.git

2. Crear entorno virtual

    - python -m venv .venv

3. Activar entorno virtual

    - .venv\Scripts\activate

4. Instalar dependencias

     - pip install django faker

5. Ejecutar migraciones

    - python manage.py migrate

6. Crear superusuario

    - python manage.py createsuperuser

        - usuario: admin  
        - contraseña: 123

7. Ejecutar servidor

    - python manage.py runserver

## Rutas importantes

/ → página principal  
/cargo/list/ → lista de cargos  
/empleado/list/ → lista de empleados  
/tarea/list/ → lista de tareas  
/about/ → información del alumno  
/admin/ → panel de administración