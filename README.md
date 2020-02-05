
- [Overview](#overview)
- [Preparation](#preparation)
- [Deployment](#deployment)
    - [Docker](#docker)
    - [Heroku](#heroku)
- [Reset](#reset)
- [Django Concept](#django-concept)
- [Authentication vs Authorization](#authentication-vs-authorization)
- [Reference](#reference)



## Overview
The prototype:
- It's deployed on: https://gentle-ridge-32032.herokuapp.com/
- Its API endpoints: https://gentle-ridge-32032.herokuapp.com/api/, to be able to check all of the APIs, an account to login is needed
- For the purpose of authentication, a visitor account is provided in the login page: https://gentle-ridge-32032.herokuapp.com/auth/login/

To familiarize with Django, jump to [Django 101](django_101.md) for details.

Functions: 
- User: register, login, logout
- Master/Detail: show folllowings' images
- Comments/Likes: like/unlike, comment
- Friends: follow/unfollow, following/follower
- Content: images upload

Note that instruction below is specifically for Mac, windows can be a bit different.


## Preparation
Install software and tools to be used:
- Homebrew: software package management system for Mac
- Python: interpreted, high-level, general-purpose programming language
- virtualenv: manage python packages in virtual environment
- Docker: run application locally
- Heroku: deploy application in the cloud

1. Install Homebrew:
```sh
# check https://brew.sh/
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
2. Install Python via Homebrew: `brew install python3`
3. Install virtualenv via pip: `pip install virtualenv`
4. Install [Docker](https://www.docker.com/products/docker-desktop) then run. 
5. Install [Heroku](https://devcenter.heroku.com/articles/heroku-cli) and register
6. Create a virtual enviroment for the project via `virtualenv`:
```sh
# create a virtual enviroment called venv
virtualenv -p /usr/local/bin/python3 venv

# activate the virtual environment
source venv/bin/activate
```
7. Install all other necessary python packages via `pip install -r application/requirements.txt`

Run `deactivate` to exit the virtual environment if needed.


## Deployment
### Docker
Docker is quite convenient to run the application locally, follow steps below to run the application via Docker:
1. Get into current project directory
2. Prepare "Dockerfile" and "docker-compose.yml" for configuration
3. Run `docker-compose up -d` to setup the application through "Dockerfile" and "docker-compose.yml"
4. Open the browser and check "http://localhost:8000/", the application is already running at the backend

To stop the application, check and stop the corresponding Docker container. Step 3 to 5 are for the purpose of clean-up:
1. Check the container ID via `docker ps -a`
2. Stop the container `docker stop {container_ID}`
3. Delete the container `docker rm {container_ID}`
4. Check the image ID `docker images`
5. Delete the corresponding image `docker rmi {image_ID}`

### Heroku
Heroku is a cloud application platform, which allows developers to deploy applications on. 

Below is those python packages needed for Heroku deployment:
- gunicorn: WSGI http server for unix
- pillow: Imaging library
- whitenoise: Simplified static file serving for web applications, which makes static files uploaded possible

If not directly clone from this project, ensure to create file "Procfile" for deployment under root directory with following content:
```sh
web: gunicorn {project_path}.wsgi --log-file -
```

Follow steps below to deploy the application on Heroku:
1. Run `source venv/bin/activate` to activate the virtual environment
2. Run `heroku login` to use Heroku CLI
3. Ensure Django and all packages related is installed `pip install -r application/requirements.txt`
4. Create a new Heroku app to deploy the project: 
```sh
heroku create

# add the Heroku app as a remote site if current project is git
git remote -v
```
5. Update "seetings.py":
    - add `'whitenoise.runserver_nostatic',` in INSTALLED_APPS
    - add `'whitenoise.middleware.WhiteNoiseMiddleware',` in MIDDLEWARE
    - add `STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')` at the end
    - add `STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'` at the end
6. Run `heroku ps:scale web=1` to use one web server only other than many.


Steps above is only needed to configure and run once, run commands below to update the project in Heroku.
```sh
source venv/bin/activate
heroku login

# add and commit all the changes
git add .
git commit -m "Deploy to Heroku"

git push heroku master

# open the web app
heroku open
```

__NOTE THAT__ since "db.sqlite3" is needed for Heroku, as well as "static/images/", remember to remove or comment them in ".gitignore" to make another commit before deployment. After deployment, reset ".gitignore" to avoid accidentally uploading the DB in the public git repository with sensitive data leak.
```sh
git reset HEAD~1
git checkout .gitignore
```


## Reset
To reset existing database and files, follow steps:
1. Remove any existing migrations:
```sh
find . -path "application/*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "application/*/migrations/*.pyc"  -delete
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

To remove current virtual environment: `rm -r venv`

To remove the Heroku branch: `git remote rm heroku`



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
