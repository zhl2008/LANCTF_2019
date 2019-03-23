#!/bin/sh
service apache2 start
chmod 777 /var/www/html
chown root:root /var/www/html/index.php
/bin/bash
