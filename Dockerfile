FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN ["pip", "install", "pipenv"]
COPY . /code
RUN ["pipenv", "install", "django"]
# RUN ["pipenv", "run", "python", "manage.py", "runserver"]