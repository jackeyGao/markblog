#!/bin/bash
# File Name: docker-entrypoint.sh
# Author: JackeyGao
# mail: junqi.gao@shuyun.com
# Created Time: 五  9/25 10:31:45 2015

/code/manage.py syncdb --noinput

echo "from django.contrib.auth.models import User
if not User.objects.filter(username='admin').count():
    User.objects.create_superuser('admin', 'admin@example.com', 'pass')
" | python manage.py shell


/usr/local/bin/gunicorn wsgi:application -w 2 -b :8000
