#!/bin/bash

airflow db init
airflow users create -e admin@example.com -f admin -l admin -p admin -r Admin -u admin
airflow scheduler &
exec airflow webserver
