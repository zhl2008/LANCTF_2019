#!/bin/bash
chown root:root /var/www/html -R

chmod 777 /var/www/html/uploads
chmod 444 /var/www/html/xxxxxxxxxasdasf_flag.php
chown root:root /var/www/html/xxxxxxxxxasdasf_flag.php

sed -i "s/;session.upload_progress.enabled = On/session.upload_progress.enabled = Off/g" /etc/php5/apache2/php.ini

source /etc/apache2/envvars
tail -F /var/log/apache2/* &
exec apache2 -D FOREGROUND
service apache2 start
