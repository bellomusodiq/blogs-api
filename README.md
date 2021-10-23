# Blogs API

clone repository

create a python3 vitrual enviroment

install dependencies
`pip install -r requirements.txt`

setup postgres database

add .env.dev to root folder with the following
```
DEBUG=
SECRET_KEY=
SQL_ENGINE=
SQL_DATABASE=
SQL_USER=
SQL_PASSWORD=
SQL_HOST=
SQL_PORT=
```

run migrations
`python manage.py migrate`

run server
`python manage.py runserver 0.0.0.0:8000`

you can change port