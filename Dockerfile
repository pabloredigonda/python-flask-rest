FROM python:3.7.1

LABEL Author="Pablo Redigonda"
LABEL E-mail="pabloredigonda@gmail.com"
LABEL version="1.0.0"

ENV PYTHONDONTWRITEBYTECODE 1
ENV FLASK_APP "src/app.py"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True

RUN mkdir /app
WORKDIR /app

RUN touch /app/Pipfile
RUN pip install --upgrade pip
RUN pip install flask
RUN pip install pipenv
RUN pip install pytest
RUN pip install flask_restful
RUN pip install flask-mongoengine
RUN pip install flask_jwt_extended
RUN pip install -U python-dotenv
RUN pipenv --python 3.7.1
RUN pip --version
RUN pipenv --version
RUN pipenv --support
RUN pipenv install --dev --system --deploy --skip-lock

ADD . /app

EXPOSE 5000

CMD flask run --host=0.0.0.0