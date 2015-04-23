#!/bin/bash
cd ~/Workspace/fk-testing
source .venv/bin/activate
rm db.sqlite3
find . -name "*.pyc" -exec rm -rf {} \;
find . -type d -name '__pycache__' -exec rm -rf {} \;
rm -rf fk_testing/apps/people/migrations/
./manage.py makemigrations people
./manage.py migrate
rm db.sqlite3
