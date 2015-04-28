#!/bin/bash

log_path='/var/log/uwsgi'
[ -d $log_path ] || mkdir -p $log_path

echo "Will Kill uWsgi."
ps -ef | grep uwsgi | grep -v grep | awk '{print $2}' | xargs -n 1 kill -9
echo "Killed! Will start uWsgi."

uwsgi -s :9000 -M -p 6 -t 30 -d $log_path/uwsgi.log --max-requests 500 --log-maxsize 50000000 --log-x-forwarded-for --log-format '%(addr) [%(ltime)] "%(method) %(uri) %(proto)" Status:%(status) %(size) "%(uagent)" %(var.HTTP_AUTHORIZATION)'  --no-site --vhost --harakiri 600

