#!/bin/sh
# launcher.sh
# run web server and sensor script on startup

cd /
cd home/ubuntu/teleco

sudo python3 telecoweb/manage.py runserver 192.168.1.169:8000

cd /
