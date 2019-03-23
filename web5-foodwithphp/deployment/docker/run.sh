#!/bin/bash
chown root:root /var/www/html -R
chown -R mysql:mysql /var/lib/mysql /var/run/mysqld
# initialize database
mysqld_safe --skip-grant-tables&
sleep 5
## change root password
mysql -uroot -e "use mysql;UPDATE user SET password=PASSWORD('icq!@#qwe') WHERE user='root';FLUSH PRIVILEGES;"
## restart mysql
service mysql restart
## execute sql file
mysql -uroot -picq\!\@\#qwe < /root/a.sql

chmod 444 /var/www/html/flag_0ba7bc92fcd57e337ebb9e74308c811f
chown root:root /var/www/html/flag_0ba7bc92fcd57e337ebb9e74308c811f
sed -i "s/;session.upload_progress.enabled = On/session.upload_progress.enabled = Off/g" /etc/php5/apache2/php.ini

source /etc/apache2/envvars
tail -F /var/log/apache2/* &
exec apache2 -D FOREGROUND
service apache2 start
