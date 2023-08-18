
Mi Proyecto Web Django
¡Bienvenido a mi proyecto web desarrollado con Django!

Este es un proyecto web creado utilizando Django, un framework de Python para el desarrollo rápido de aplicaciones web. El objetivo principal de este proyecto es demostrar cómo construir un sitio web con las siguientes funcionalidades:

Mostrar una página de inicio con enlaces a otras secciones del sitio.
Permitir la inserción, edición y eliminación de datos de recetas en la base de datos.
Registro y autenticación de usuarios.
Realizar búsquedas en la base de datos de recetas.
Requisitos
Antes de ejecutar el proyecto, asegúrate de tener instalado lo siguiente:

Python: Este proyecto ha sido desarrollado y probado con Python 3.x.
Django: Asegúrate de tener instalado Django en tu entorno virtual.
Configuración
Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local:

Clona el repositorio en tu máquina local:

bash
Copy code
git clone https://github.com/tu-usuario/proyecto-web-django.git
Crea un entorno virtual e instala las dependencias:

bash
Copy code
cd proyecto-web-django
python -m venv env
source env/bin/activate  # En Windows: env\Scripts\activate
pip install -r requirements.txt
Realiza las migraciones para crear la base de datos:

bash
Copy code
python manage.py migrate
Ejecuta el servidor de desarrollo:

bash
Copy code
python manage.py runserver
Accede al sitio web en tu navegador:

bash
Copy code
http://localhost:8000/
Estructura del Proyecto
La estructura del proyecto es la siguiente:

lua
Copy code
proyecto-web-django/
|-- README.md
|-- manage.py
|-- proyecto/
|   |-- __init__.py
|   |-- settings.py
|   |-- urls.py
|   |-- views.py
|   |-- forms.py
|   |-- models.py
|   |-- admin.py
|   |-- templates/
|   |   |-- base.html
|   |   |-- index.html
|   |   |-- insertar_datos.html
|   |   |-- recetas.html
|   |   |-- usuario.html
|   |-- static/
|   |   |-- styles.css
|   |-- migrations/
|-- env/
|-- requirements.txt
proyecto: Esta es la aplicación principal del proyecto, donde se encuentra el archivo settings.py, las vistas (views.py), los modelos (models.py), los formularios (forms.py) y las plantillas HTML en el directorio templates/.

static: Contiene archivos estáticos como hojas de estilo (CSS) y archivos JavaScript.

migrations: Contiene las migraciones de la base de datos generadas por Django.

Funcionalidades
El proyecto incluye las siguientes funcionalidades:

Página de Inicio (index): Muestra una página de inicio con enlaces a otras secciones del sitio.

Inserción, Edición y Eliminación de Datos: Permite ingresar, editar y eliminar datos de recetas en la base de datos a través de formularios.

Registro y Autenticación de Usuarios: Los usuarios pueden registrarse, iniciar sesión y actualizar sus perfiles.

Búsqueda de Recetas: Proporciona un formulario para buscar recetas en la base de datos según un término de búsqueda.