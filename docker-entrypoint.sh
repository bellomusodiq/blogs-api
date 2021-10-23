#!/bin/bash

echo "Migrate the Database at startup of project"

# Wait for few minute and run db migraiton
while ! python manage.py makemigrations  2>&1; do
   echo "Make migration is in progress status"
   sleep 3
done

# Wait for few minute and run db migraiton
while ! python manage.py migrate  2>&1; do
   echo "Migration is in progress status"
   sleep 3
done

echo "Django docker is fully configured successfully."

exec "$@"