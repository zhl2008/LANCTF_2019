#!/bin/sh
docker run -v `pwd`/../source:/var/www/html -v `pwd`:/root/ -p 8011:8000 -tid icq:py3s /root/run.sh
