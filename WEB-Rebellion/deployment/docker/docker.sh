#!/bin/sh
docker run -v `pwd`/../source:/var/www/html -v `pwd`:/root/ -p 80:80 -tid icq:14.04 /root/run.sh
