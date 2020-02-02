
- [Mini Instragram](#mini-instragram)
    - [Overview](#overview)
    - [Preparation](#preparation)
        - [Installation](#installation)
        - [Initialization](#initialization)
    - [Structure](#structure)
    - [Development](#development)
        - [Component](#component)
        - [External Library](#external-library)
        - [Model](#model)
        - [View](#view)
    - [Reset](#reset)
    - [Other](#other)
- [Deployment](#deployment)
    - [Docker](#docker)
    - [Heroku](#heroku)
- [Django Concept](#django-concept)
- [Authentication vs Authorization](#authentication-vs-authorization)
- [Reference](#reference)

# Mini Instragram
Instructions below is for Mac specifically, windows can be a bit different.

For example, the prototype is implemented and deployed on: https://gentle-ridge-32032.herokuapp.com/


## Overview
Functions: 
- User: register, login, logout
- Master/Detail: show folllowings' images
- Comments/Likes: like/unlike, comment
- Friends: follow/unfollow, following/follower
- Content: images upload

Toolkit: git, homebrew, pipenv, heroku


## Preparation

### Installation
Install software and tools to be used:
- Xcode tool:
- Homebrew: software package management system for Mac
- Python: interpreted, high-level, general-purpose programming language
- virtualenv: manage python packages in virtual environment

1. Install Xcode tool chain and Homebrew:
```sh
xcode-select --install

# check https://brew.sh/
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
2. Install Python via Homebrew: `brew install python3`
3. Install virtualenv via pip: `pip install virtualenv`

### Initialization
For any new project, follow steps below:
1. Create a directory for the project
```sh
mkdir MiniInstagram
cd MiniInstagram
```
2. Create a virtual enviroment for the project
```sh
# create a virtual enviroment called venv
virtualenv -p /usr/local/bin/python3 venv

# activate the virtual environment
source venv/bin/activate

# deactivate the virtual environment if needed
deactivate
```
3. Create the Django project
```sh
# install Django inside the project via pipenv: 
pip install django

# create the Django project with an identifiable name under current directory
django-admin startproject {project} .
```
4. Run the project to verify http://localhost:8000/ is working properly, a SQLite DB should be created accordingly: 
```py
python manage.py runserver
```
5. Create an admin user for the project
```py
# migrate all default apps
python manage.py migrate
# After migration, create an admin user for the project: 
python manage.py createsuperuser
```
6. Log in as the admin user via http://localhost:8000/admin/
7. Press CONTROL-C to quit
8. Deactivate the virtual environment: `exit`
9. Create a template directory for html files and map it in "{project}/setting.py"
```py
TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, '{templates}')],
        ...
    },
]
```


## Structure
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
- Pipfile: Django packages meta
- Pipfile.lock: Django packages details


## Development

### Component
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

### External Library
Install 3rd party below to support more functionalities:
```sh
# install for better image rendering
pipenv install django-imagekit
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

### Model
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

### View
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


### API
To develop the RESTful(Representational State Transfer) API in Django, the framework package is needed: `pipenv install djangorestframework`

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


## Deployment
### Docker
Docker is quite convenient to run the application locally, follow steps below to run the application via Docker:

1. Install the [Docker](https://www.docker.com/products/docker-desktop) then run
2. Get into current project directory
3. Run `docker-compose up -d` to setup the application through "Dockerfile" and "docker-compose.yml"
4. Open the browser and check "http://localhost:8000/", the application is already running at the backend

To stop the application, check and stop the corresponding Docker container. Step 3 to 5 are for the purpose of clean-up:
1. Check the container ID via `docker ps -a`
2. Stop the container `docker stop {container_ID}`
3. Delete the container `docker rm {container_ID}`
4. Check the image ID `docker images`
5. Delete the corresponding image `docker rmi {image_ID}`


### Heroku
If not directly clone from this project, make sure:

1. Install package gunicorn and pillow: 
```sh
pipenv install gunicorn
pipenv install pillow
```

2. Create file "Procfile" for deployment under root directory:
```sh
web: gunicorn {procjt}.wasgi --log-file -
```

Since `pipenv` has already set up the configuration in this project, follow steps below at first run:

1. Install [Heroku](https://devcenter.heroku.com/articles/heroku-cli).

2. Register Heroku then run `heroku login` to use Heroku CLI.

3. Run `pipenv shell` to create/activate a virtual environment.

4. Ensure Django and all packages related is installed 
```sh
pipenv lock

pipenv install django
```

5. Create a new Heroku app to deploy the project: 
```sh
heroku create

# it would add the app as a remove site if current project is git
git remote -v
```

6. Install package "whitenoise" to make static files uploaded possible `pipenv install whitenoise`.

7. Update "seetings.py":
- add `'whitenoise.runserver_nostatic',` in INSTALLED_APPS
- add `'whitenoise.middleware.WhiteNoiseMiddleware',` in MIDDLEWARE
- add `STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')` at the end
- add `STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'` at the end

8. Run `heroku ps:scale web=1` to use web server (one only) other than many.


Steps above is only needed to be configured and run once, run commands below to deploy/update the project in Heroku.
```sh
# add and commit all the changes
git add .
git commit -m "Deploy to Heroku"

git push heroku master

# open the web app
heroku open
```

__NOTE THAT__ since "db.sqlite3" is needed for Heroku, as well as "static/images/", remember to remove/comment them in .gitignore and make another commit before deployment. After deployment, reset .gitignore to avoid accidentally uploading the DB in public git repository and sensitive data leak.
```sh
git reset HEAD~1
git checkout .gitignore
```


## Reset
To reset existing database and files, follow steps:
1. Remove any existing migrations:
```sh
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc"  -delete
```
2. Remove existing database and static files (make sure it's expected since everything would be cleanup):
```sh
rm db.sqlite3
rm -r static/images
```
3. Regenerate migrations and database schema:
```sh
python manage.py makemigrations
python manage.py migrate
```

To remove current virtual environment: `pipenv --rm`

To remove the Heroku branch: `git remote rm heroku`


## Other
{%  %}: template language
{{  }}: variable

Class-based view vs Function view

Django would generate a plural variable which is equal to `object_list` in the html, like `posts` for model Post.

Install django-annoying for toggling like icon: `pipenv install django-annoying`

`pipenv lock`: check all the packages are updated



# Django Concept

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



# Authentication vs Authorization
- Authentication is to check who you are, while Authorization is to determine what you can do
- Like taking a flight:
    - authentication: ID is to prove who you are 
    - authorization: the flight ticket is to verify you are permitted to onboard
- Like in a forum:
    - authentication: account and password are to prove who you are 
    - authorization: the permissions you have



# Reference
- Classy Class-Based Views: https://ccbv.co.uk/
- Generic display views: https://docs.djangoproject.com/en/2.2/ref/class-based-views/generic-display/
- Customizing authentication in Django: https://docs.djangoproject.com/en/2.2/topics/auth/customizing/
- Django Templates: https://docs.djangoproject.com/en/2.2/topics/templates/
- Custom template tags and filters: https://docs.djangoproject.com/en/2.2/howto/custom-template-tags/
- Access Mixins: https://django-braces.readthedocs.io/en/latest/access.html
- JiuZhang demo: https://github.com/yibeibaoke/InstaDemo
- Django Rest framework: https://www.django-rest-framework.org/
- Implement Token Authentication using Django REST Framework: https://simpleisbetterthancomplex.com/tutorial/2018/11/22/how-to-implement-token-authentication-using-django-rest-framework.html
- How to Reset Migrations: https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html
- SQLLite Viewer: http://sqliteviewer.flowsoft7.com/
