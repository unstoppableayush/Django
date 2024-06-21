# How to Create a Model in Django 

- First We have to make a app to create a model

- Create a `service` app : `python manage.py startapp service`

- Creation od Model :
> models.py
```python
from django.db import models

# Create your models here.

class Service(models.Model):
    #fields
    service_icon = models.CharField(max_length=50)
    service_title = models.CharField(max_length=50)
    service_des = models.TextField()
```

- Register your app:
> settings.py
```python
INSTALLED_APPS = [
    'service'
]
```
- Run Migration - `python manage.py makemigrations`

- Now a modal of service name or migration file created with required fields .

- To convert models into table : 
`python manage.py migrate`

- To create options in admin :
   -  Import models in `admin.py`
   -  create a class and add fields you want to show in admin `list_display=('')` 
   - Register the the model and function.

> admin.py
```python
from django.contrib import admin
from service.models import Service
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_icon','service_title','service_des')

admin.site.register(Service, ServiceAdmin)

```


