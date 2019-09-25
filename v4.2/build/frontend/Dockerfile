FROM nginx:latest

RUN apt-get update && apt-get install --no-install-recommends -y git && apt-get clean \
 && apt-get autoclean && apt-get autoremove -y -qq

RUN rm -rf /app
WORKDIR /app

RUN git config --global http.sslVerify false
RUN git clone https://github.com/taigaio/taiga-front-dist .
RUN git checkout stable
RUN git checkout tags/4.2.12 -b "4.2.12"
RUN mv ./dist/* ./
RUN rm -rf dist

COPY conf.json /app/conf.json
COPY run.sh /app/run.sh
COPY nginx.conf /etc/nginx/nginx.conf
COPY taiga.conf /etc/nginx/conf.d/default.conf

ADD scripts/letsencrypt-auto /opt/letsencrypt/letsencrypt-auto
RUN chmod +x /opt/letsencrypt/letsencrypt-auto; /opt/letsencrypt/letsencrypt-auto --os-packages-only --install-only --non-interactive;
RUN chmod -R 755 /app && chmod +x /app/run.sh
RUN groupadd -r -g 2000 taiga; useradd -r -u 2000 -g 2000 -m -c "app account" -d /home/taiga -s /bin/bash taiga

CMD ["/app/run.sh"]
