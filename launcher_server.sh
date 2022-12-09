#!/bin/sh
# launcher.sh
# run web server and sensor script on startup

cd /
cd home/pablo/teleco

sudo source bin/activate
sudo python telecoweb/manage.py runserver 192.168.1.169:8000

cd /
