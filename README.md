[![Build Status](https://travis-ci.com/trydirect/taiga.svg?branch=master)](https://travis-ci.com/trydirect/taiga)
![Docker Stars](https://img.shields.io/docker/stars/trydirect/taiga.svg)
![Docker Pulls](https://img.shields.io/docker/pulls/trydirect/taiga.svg)
![Docker Automated](https://img.shields.io/docker/cloud/automated/trydirect/taiga.svg)
![Docker Build](https://img.shields.io/docker/cloud/build/trydirect/taiga.svg)
[![Gitter chat](https://badges.gitter.im/trydirect/community.png)](https://gitter.im/try-direct/community)
	
	
# Taiga 
The goal of this project is to give possibility to setup taiga as easy as it possible.


## Installation
Clone this project into your work directory:
```sh
$ git clone "https://github.com/trydirect/taiga.git"
$ cd taiga
```
Run services:
```sh
$ docker-compose up -d
```

## Finish Setup
In order to create django database structure and apply migrations execute following command:
```
docker-compose exec --user=taiga taigaback scripts/setup.sh
```


## Quick deployment to cloud
##### Amazon AWS, Digital Ocean, Hetzner and others
[<img src="https://img.shields.io/badge/quick%20deploy-%40try.direct-brightgreen.svg">](https://try.direct/server/user/deploy/InRhaWdhfDZ8MjUi.EAoFeA.VyIeETvchuZZNNqIg1UUNGytFZo/)



## Contributing

1. Fork it (https://github.com/trydirect/taiga/fork)
2. Create your feature branch (git checkout -b feature/fooBar)
3. Commit your changes (git commit -am 'Add some fooBar')
4. Push to the branch (git push origin feature/fooBar)
5. Create a new Pull Request
