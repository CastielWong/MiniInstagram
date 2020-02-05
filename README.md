
- [Overview](#overview)
- [Preparation](#preparation)
- [Deployment](#deployment)
    - [Docker](#docker)
    - [Heroku](#heroku)
- [Reset](#reset)
- [Django Concept](#django-concept)
- [Authentication vs Authorization](#authentication-vs-authorization)
- [Reference](#reference)


The prototype is implemented and deployed on: https://gentle-ridge-32032.herokuapp.com/

To familiarize with Django, jump to [Django 101](django_101.md) for details.

Instructions below is for Mac specifically, windows can be a bit different.

## Overview
Functions: 
- User: register, login, logout
- Master/Detail: show folllowings' images
- Comments/Likes: like/unlike, comment
- Friends: follow/unfollow, following/follower
- Content: images upload

Toolkit: git, homebrew, virtualenv, heroku


## Preparation

Install software and tools to be used:
- Homebrew: software package management system for Mac
- Python: interpreted, high-level, general-purpose programming language
- virtualenv: manage python packages in virtual environment

1. Install Homebrew:
```sh
# check https://brew.sh/
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
2. Install Python via Homebrew: `brew install python3`
3. Install virtualenv via pip: `pip install virtualenv`
4. Create a virtual enviroment for the project via `virtualenv`:
```sh
# create a virtual enviroment called venv
virtualenv -p /usr/local/bin/python3 venv

# activate the virtual environment
source venv/bin/activate
```
5. Install all other necessary python packages via `pip install -r application/requirements.txt`

Run `deactivate` to exit the virtual environment if needed.



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
pip install gunicorn
pip install pillow
```

2. Create file "Procfile" for deployment under root directory:
```sh
web: gunicorn {procjt}.wasgi --log-file -
```

Since the configuration for this project is set up, follow steps below at first run:

1. Install [Heroku](https://devcenter.heroku.com/articles/heroku-cli).

2. Register Heroku then run `heroku login` to use Heroku CLI.

3. Run `source venv/bin/activate` to activate a virtual environment.

4. Ensure Django and all packages related is installed 
```sh
pip install -r requirements.txt
```

5. Create a new Heroku app to deploy the project: 
```sh
heroku create

# it would add the app as a remove site if current project is git
git remote -v
```

6. Install package "whitenoise" to make static files uploaded possible `pip install whitenoise`.

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
