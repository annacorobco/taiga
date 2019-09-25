FROM ubuntu:18.04

MAINTAINER Optimum "info@optimum-web.com"

RUN groupadd -r -g 2000 taiga; useradd -r -u 2000 -g 2000 -m -c "app account" -d /home/taiga -s /bin/bash taiga

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

RUN pip3 install wheel==0.33.4 uwsgi==2.0.18

WORKDIR /app

RUN git config --global http.sslVerify false
RUN git clone https://github.com/taigaio/taiga-back.git .
RUN git checkout stable
# RUN git checkout tags/4.2.12 -b "4.2.12"

COPY wsgi.ini /etc/taiga-wsgi.ini
COPY taiga.conf /etc/supervisor/conf.d/taiga.conf
COPY docker-settings.py /app/settings/local.py
# temporary fix https://github.com/taigaio/taiga-back/issues/904#issuecomment-323512014
RUN rm /app/taiga/base/api/serializers.py
COPY serializers.py /app/taiga/base/api/serializers.py

RUN chown taiga.taiga -R /app

RUN pip3 install -r requirements.txt

EXPOSE 8000
