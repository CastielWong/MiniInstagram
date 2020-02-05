FROM python:3.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN pip install virtualenv
RUN python3 -m virtualenv --python=/usr/local/bin/python3 /code/venv
RUN . /code/venv/bin/activate
COPY application/ /code
RUN pip install -r requirements.txt
