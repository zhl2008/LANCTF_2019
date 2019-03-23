#!/bin/sh
cp /root/000-default.conf /etc/apache2/sites-enabled/000-default.conf
a2enmod rewrite
service apache2 start
/bin/bash
