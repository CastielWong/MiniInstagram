
- [Concept](#concept)
    - [Authentication vs Authorization](#authentication-vs-authorization)
- [Structure](#structure)
- [Initialization](#initialization)
- [Development](#development)
    - [Component](#component)
    - [External Library](#external-library)
    - [Model](#model)
    - [View](#view)
    - [API](#api)
    - [Other](#other)
    

# Concept
Framework includes:
- Middlleware
- Library
- API
- Coding shortcuts
- Performance boosting
- Caching
- Security

Django includes:
- User authentication
- Templates, routes and views
- Admin interface
- Robust security
- Multiple databases supported

## Authentication vs Authorization
- Authentication is to check who you are, while Authorization is to determine what you can do
- Like taking a flight:
    - authentication: ID is to prove who you are 
    - authorization: the flight ticket is to verify you are permitted to onboard
- Like in a forum:
    - authentication: account and password are to prove who you are 
    - authorization: the permissions you have


# Structure
Normally, a Django __project__ includes multiple __app__, each app is responsible for a particular function like Auth, Payment etc.

The general structure of the project:
- {project}: core of the Django project, includes configuration files
    - \_\_init\_\_.py: initialization placeholder
    - settings.py: global configuration
    - urls.py: decide where the URL is matched to at project level
    - wsgi.py: Web Server Gateway Interface, which needed by Apache
- {app}: each component
    - migrations: track the changes between Django model and the database, which is used to synchronize DB migration
        - \_\_init\_\_.py: initialization placeholder
        - 000x_xxx.py: migrations history tracks
    - \_\_init\_\_.py: initialization placeholder
    - admin.py: for admin configuration
    - apps.py: the configuration at app level, which is corresponding to the settings.py
    - models.py: __MODEL__, Django can convert it into DB tables
    - tests.py: app-specific tests
    - views.py: __CONTROLLER__, used to process request/response
    - forms.py
    - urls.py: can be created to decide where the URL is matched to at app level
- static: resources
    - images
    - profiles
- templates: __VIEW__, all html templates
- manage.py: run Django commands


# Initialization
For any new project, follow steps below:
1. Create a directory for the project
```sh
mkdir MiniInstagram
cd MiniInstagram
```

2. Create the Django project, run `pip install django` if it's not installed:
```sh
mkdir application
cd application

# create the Django project with an identifiable name under current directory, which includes configurations
django-admin startproject {project} .
```

3. Run the project to verify http://localhost:8000/ is working properly, a SQLite DB should be created accordingly: 
```py
python manage.py runserver
```

4. Create an admin user for the project, follow the prompt to set up username and password:
```py
# migrate all default apps
python manage.py migrate
# create an admin user for the project after migration
python manage.py createsuperuser
```

5. Log in as the admin user via http://localhost:8000/admin/
6. Press CONTROL-C to quit
7. Create a template directory to keep all html files under current directory, then map it in "{project}/setting.py"
```py
TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, '{templates}')],
        ...
    },
]
```


# Development

## Component
1. Create a new app for the component: `python manage.py startapp {new_app}`
2. Connect the project and app in "settings.py", for example:
```py
...
INSTALLED_APPS = [
    ...,
    'new_app',
]
...
```

## External Library
Install 3rd party below to support more functionalities:
```sh
# install for better image rendering
pip install django-imagekit
# pillow is needed for the Python Imaging Library
pip install pillow
```

Remember to add them into "settings.py" to enable:
```py
...
INSTALLED_APPS = [
    ...,
    'imagekit',
    ...
]
```

## Model
1. Create a new model in "models.py", note that the image path would be created automatically if doesn't exist yet
2. Synchronize model with database:
```py
# `makemigrations` would check the difference between all current models and migrations files in the apps
python manage.py makemigrations
# migrate would take all migrations files to synchronize models into database
python manage.py migrate
```
3. Register the app's model in admin page.
```py
from {app}.models import Post

admin.site.register({model})
```

Note that for each model created, Django would add an auto-incremented primary key field automatically, which can be accessed via `pk` or `id`. For example, we can use it into path in "urls.py", like `path('{path}/<int:pk>', ...)`.

## View
Append `STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]` in "settings.py" to make sure Django knows where to find static files. 

View in Django is corresponding to the Controller part in MVC, below shows steps in general to configure View.

1. Configure View in "views.py", for example:
```py
from django.views.generic import TemplateView

class HelloDjango(TemplateView):
    template_name = 'index.html'
```
2. Configure URLConfs:
    1. In app level, create a "urls.py" to manage the inside URLConfiguration
    ```py
    from django.urls import path

    from . import views

    urlpatterns = [
        path('', views.HelloDjango.as_view()),
    ]
    ```
    2. In project level, update urls.py:
    ```py
    from django.urls import path, include

    urlpatterns = [
        ...,
        path('{path}/', include('{app}.urls')),
    ]
    ```
3. Create corresponding html under templates directory, note that remember to put '/' for relative path to ensure the source is retrived, like `<img src="/{file}">`. 


## API
To develop the RESTful (Representational State Transfer) API in Django, the framework package is needed: `pip install djangorestframework`

Follow steps below to set up the API:
1. Update "seetings.py":
    - add `'rest_framework',` in INSTALLED_APPS
    - append codes below for pagination
    ```py
    REST_FRAMEWORK = {
        'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
        'PAGE_SIZE': 10
    }
    ```
2. Create serializers for the models
    - inherit different `ModelSerializer` for each model if needed
    - set up the fields and their corresponding permission
3. Create ViewSet in "views.py" (app or project level)
    - setup `queryset`
    - set up `serializer_class`
    - add `permission_classes` for authentication if needed
4. Configure the path in "urls.py" (project level)


## Other
{%  %}: template language
{{  }}: variable

Class-based view vs Function view

Django would generate a plural variable which is equal to `object_list` in the html, like `posts` for model Post.

Install django-annoying for toggling like icon: `pip install django-annoying`
