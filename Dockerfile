FROM python:3.9.9

WORKDIR /home/

RUN git clone https://github.com/tourbut/tourbut.git

WORKDIR /home/tourbut/

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY=django-insecure-6nt5wfffks93mj9%a1ni8*@0m(qs-det95ok%j#!@vn5u8$lkn" > .env

RUN python manage.py makemigrations

RUN python manage.py migrate

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]