#!/bin/sh
service apache2 start
python /var/www/html/delete.py & 
/bin/bash
