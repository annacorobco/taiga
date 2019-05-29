FROM nginx

RUN apt-get update && apt-get install -y git

RUN rm -rf /app

WORKDIR /app

RUN git clone https://github.com/taigaio/taiga-front-dist .
RUN git checkout stable
RUN mv ./dist/*  ./
RUN rm -rf dist

COPY conf.json /app/conf.json
COPY run.sh /app/run.sh
COPY nginx.conf /etc/nginx/nginx.conf
COPY taiga.conf /etc/nginx/conf.d/default.conf

ADD ./scripts/letsencrypt-auto /opt/letsencrypt/letsencrypt-auto

RUN chmod +x /opt/letsencrypt/letsencrypt-auto; /opt/letsencrypt/letsencrypt-auto  --os-packages-only --install-only --non-interactive;

RUN chmod -R 755 /app && chmod +x /app/run.sh
RUN groupadd -r -g 2000 taiga; useradd -r -u 2000 -g 2000 -m -c "app account" -d /home/taiga -s /bin/bash taiga


CMD ["/app/run.sh"]
