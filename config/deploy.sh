x#!/usr/bin/env bash

cd /opt/apps/career-studio/
git pull origin master
source /home/admin/.virtualenvs/career-studio/bin/activate
pip install -r /opt/apps/career-studio/requirements.txt
/home/admin/.virtualenvs/career-studio/bin/python manage.py migrate
/home/admin/.virtualenvs/career-studio/bin/python manage.py collectstatic --noinput
sudo supervisorctl stop career-studio
kill $(lsof -t -i:8035)
sudo supervisorctl start career-studio
