FROM ubuntu:18.04

MAINTAINER Optimum "info@optimum-web.com"

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get autoremove -y && apt-get --no-install-recommends -y install locales supervisor curl \
 gcc libpq5 git libpcre3-dev lsof net-tools libpq-dev uwsgi uwsgi-src uuid-dev libcap-dev gettext build-essential libssl-dev \
 libffi-dev python3-dev zlib1g-dev python3-pip python3-setuptools && apt-get clean && apt-get autoclean

RUN locale-gen en_US.UTF-8 && dpkg-reconfigure locales
COPY locale.gen /etc/locale.gen
COPY default.locale /etc/default/locale

# compile uwsgi plugin for python3.6
RUN PYTHON=python3.6 uwsgi --build-plugin "/usr/src/uwsgi/plugins/python python36"
RUN mv python36_plugin.so /usr/lib/uwsgi/plugins/python36_plugin.so
RUN locale -a

WORKDIR /app
RUN git config --global http.sslVerify false
RUN git clone https://github.com/taigaio/taiga-back.git .
#RUN git checkout stable
RUN git checkout tags/3.4.5 -b "3.4.5"

COPY wsgi.ini /etc/taiga-wsgi.ini
COPY taiga.conf /etc/supervisor/conf.d/taiga.conf
COPY docker-settings.py /app/settings/local.py
# temporary fix https://github.com/taigaio/taiga-back/issues/904#issuecomment-323512014
RUN rm /app/taiga/base/api/serializers.py
COPY serializers.py /app/taiga/base/api/serializers.py

RUN pip3 install wheel==0.33.4 && pip3 install -r requirements.txt && pip3 install uwsgi==2.0.18
RUN groupadd -r -g 2000 taiga; useradd -r -u 2000 -g 2000 -m -c "app account" -d /home/taiga -s /bin/bash taiga

EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
