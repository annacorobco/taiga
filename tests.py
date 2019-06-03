#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import docker
import requests

client = docker.from_env()
time.sleep(10)  # we expect all containers are up and running in 10 secs

for c in client.containers.list():
    print("{}: {}".format(c.name, c.status))
    if 'running' not in c.status:
        print(c.logs())

# NGINX
nginx = client.containers.get('taigafront')
nginx_cfg = nginx.exec_run("/usr/sbin/nginx -T")
assert nginx.status == 'running'
assert 'the configuration file /etc/nginx/nginx.conf syntax is ok' in nginx_cfg.output.decode()
assert 'HTTP/1.1" 500' not in nginx.logs()

# test restart
nginx.restart()
time.sleep(3)
assert nginx.status == 'running'

web = client.containers.get('taigaback')
assert 'setgid() to 2000' in web.logs()
assert 'setuid() to 2000' in web.logs()
assert 'spawned uWSGI master process' in web.logs()
assert 'spawned uWSGI worker 1' in web.logs()
assert 'spawned uWSGI worker 2' in web.logs()
assert 'spawned uWSGI worker 3' in web.logs()
assert 'spawned uWSGI worker 4' in web.logs()
# assert 'Internal Server Error' not in web.logs()
assert web.status == 'running'

db = client.containers.get('taigadb')
assert db.status == 'running'
cnf = db.exec_run('psql -U taiga -h 127.0.0.1 -p 5432 -c "select 1"')
log = db.logs()
assert "database system is ready to accept connections" in log.decode()

response = requests.get("http://localhost")
assert response.status_code == 200
assert "<title>Taiga</title>" in response.text
