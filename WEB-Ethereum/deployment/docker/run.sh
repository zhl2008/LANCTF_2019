#!/bin/sh
service apache2 start
chown -R mysql:mysql /var/lib/mysql /var/run/mysqld
service mysql start
mysql -uroot < /root/setup.sql
/bin/bash
