# recipe-app-api
Recipe App API source code


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