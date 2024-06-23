# Get Data from Table in Django | Objects All () 

> views.py

```python
def services(request):
    services = Service.objects.all()
    print(services)
    return render(request, 'services.html', {'services': services})
```

> urls.py

```python
 path('services/', views.services, ),
```
> services.html

```html
<body>
    {% include "header.html" %}
    {% for n in services %}
    <h1> {{n.service_icon}} | {{n.service_title}} | {{n.service_des}}  </h1>
    {% endfor %}
</body>
```
