#!/bin/sh
cd /var/www/html
useradd test
cp /root/flask.conf /etc/supervisor/conf.d/
service supervisor start
#su test -c 'python3 /var/www/html/web.py &'
#su test -c  'gunicorn -w 4 -b 0.0.0.0:8000 --daemon  web:app'
/bin/bash
