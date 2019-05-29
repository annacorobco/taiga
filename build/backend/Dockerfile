FROM python:3.6

MAINTAINER Optimum "info@optimum-web.com"

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update  && apt-get autoremove -y && apt-get -y --no-install-recommends install locales supervisor curl \
 vim gcc libpq5 git lsof net-tools libpq-dev uwsgi uwsgi-src uuid-dev libcap-dev gettext

RUN locale-gen en_US.UTF-8 && dpkg-reconfigure locales

COPY locale.gen /etc/locale.gen
COPY default.locale /etc/default/locale

# compile uwsgi plugin for python3.6
RUN PYTHON=python3.6 uwsgi --build-plugin "/usr/src/uwsgi/plugins/python python36"
RUN mv python36_plugin.so /usr/lib/uwsgi/plugins/python36_plugin.so

RUN locale -a

WORKDIR /app
RUN git clone -b stable --single-branch https://github.com/taigaio/taiga-back.git .

COPY wsgi.ini /etc/taiga-wsgi.ini
COPY taiga.conf /etc/supervisor/conf.d/taiga.conf
COPY docker-settings.py /app/settings/local.py
# temporary fix https://github.com/taigaio/taiga-back/issues/904#issuecomment-323512014
RUN rm /app/taiga/base/api/serializers.py
COPY serializers.py /app/taiga/base/api/serializers.py

RUN pip install -r requirements.txt && pip install uwsgi
RUN groupadd -r -g 2000 taiga; useradd -r -u 2000 -g 2000 -m -c "app account" -d /home/taiga -s /bin/bash taiga

EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
