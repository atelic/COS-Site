`master` COS Status: [![Build Status](https://travis-ci.org/ZobairAlijan/COS-Site.svg?branch=master)](https://travis-ci.org/ZobairAlijan/COS-Site)


# COS-Site

### Installation

`$ pip install -r requirements.txt`

`$ bower install`

`$ cp mysite/default_local_settings.py local_settings.py`

`$ brew install memcached`

`$ python manage.py migrate`

`$ python manage.py createsuperuser`

`$ python manage.py runserver`

go to http://127.0.0.1:8000


### View as Admin

`$ python manage.py runserver`

go to http://127.0.0.1:8000/admin

### Troubleshooting

1. If you see the error:
   `django.db.utils.OperationalError: could not connect to server: Connection refused`
   then you will need to start the postgres server.

   On a Mac:
   `$ pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start`

   On Linux:
   `$ sudo systemctl start postgres`
