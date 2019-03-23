#!/bin/sh
docker run -v `pwd`/../source:/var/www/html -v `pwd`:/root/ -p 8012:8000 -tid icq:py3g /root/run.sh
