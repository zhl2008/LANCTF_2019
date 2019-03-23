#!/bin/bash
sleep 1
chown root:root /var/www/html -R

sed -i "s/;session.upload_progress.enabled = On/session.upload_progress.enabled = Off/g" /etc/php5/apache2/php.ini
chmod 444 /var/www/html/xxqqwweer_flag.php
chown root:root /var/www/html/xxqqwweer_flag.php
chmod 777 /var/www/html/uploads

source /etc/apache2/envvars
tail -F /var/log/apache2/* &
exec apache2 -D FOREGROUND
service apache2 start
