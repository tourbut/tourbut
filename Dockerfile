FROM python:3.9.9

WORKDIR /home/

RUN echo "testing"

RUN git clone https://github.com/tourbut/tourbut.git

WORKDIR /home/tourbut/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient


EXPOSE 8000

CMD ["bash","-c","python manage.py collectstatic --noinput --settings=tourbut.settings.deploy && python manage.py migrate --settings=tourbut.settings.deploy && gunicorn tourbut.wsgi --env DJANGO_SETTINGS_MODULE=tourbut.settings.deploy --bind 0.0.0.0:8000"]