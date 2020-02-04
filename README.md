# Django Python Advanced TDD
Recipe App API source code
https://www.udemy.com/course/django-python-advanced/

### Start locally
```
docker-compose up
```

### Start django project
```
docker-compose run app sh -c "django-admin.py startproject app ."
```

### Run Tests
```
docker-compose run app sh -c "python manage.py test"
```

### Create an App
```
docker-compose run app sh -c "python manage.py startapp core"
```

### Make migrations on app
```
docker-compose run app sh -c "python manage.py makemigrations core"
```

### Create superuser
```
docker-compose run app sh -c "python manage.py createsuperuser"
```

### Remove container flag
```
docker-compose run --rm app sh -c "python manage.py startapp user"
```

### Seed data with migrations
```
docker-compose run --rm app sh -c "python manage.py makemigrations --empty core"
# https://docs.djangoproject.com/en/3.0/ref/migration-operations/
```

### Dump Data for fixtures
```
docker-compose run app sh -c "python manage.py dumpdata"
```

### Run fixtures
```
docker-compose run app sh -c "python manage.py loaddata auth_groups"
# https://docs.djangoproject.com/en/3.0/howto/initial-data/
```


```
Django>=2.1.0,<2.2.0
djangorestframework>=3.8.2,<3.9.0
flake8>=3.6.0,<3.7.0
```