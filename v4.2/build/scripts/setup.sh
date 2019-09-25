#!/usr/bin/env bash

docker-compose exec --user='taiga' taigaback bash -c 'pip3 install -r requirements.txt'
docker-compose exec --user='taiga' taigaback bash -c 'python3 manage.py migrate --noinput'
docker-compose exec --user='taiga' taigaback bash -c 'python3 manage.py loaddata initial_user'
docker-compose exec --user='taiga' taigaback bash -c 'python3 manage.py loaddata initial_project_templates'
