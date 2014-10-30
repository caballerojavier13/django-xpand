django-xpand
============

## Requerimientos

* [Python 3](https://www.python.org/)
* [Django](https://www.djangoproject.com/)

## Instrucciones

1. Clonar el repositorio:

  ```bash
  git clone https://github.com/MDA2014/django-xpand.git
  ```

2. Posicionarse en la carpeta del proyecto:

  ```bash
  cd django-xpand/django_project/
  ```

3. Generar la base de datos de Django:

  ```bash
  python manage.py syncdb
  ```

4. Crear las migraciones de la base de datos y aplicarlas:

  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```

5. Ejecutar el servidor Django:

  ```bash
  python manage.py runserver
  ```

6. Para ingresar desde el navegador (el puerto por defecto es el 8000):

  | Dirección                    | Descripción                                |
  |:---------------------------- |:------------------------------------------:|
  | http://127.0.0.1:8000/       | Página de inicio del proyecto              |
  | http://127.0.0.1:8000/app/   | Página de inicio de la aplicación generada |
  | http://127.0.0.1:8000/admin/ | Página de administración del proyecto      |
