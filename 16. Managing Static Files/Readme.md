# What is CSS, JavaScript & Images in Django and How to use them

We have to give permission to use static files to STATICFILES_DIRS.


```python
STATICFILES_DIRS = [
    BASE_DIR, "Static"
]
```

To user in html 

```html
 <link rel="stylesheet" href="/Static/CSS/index.css" />
```


We can also use `{% load Static %} to load static files in html.

We use this top of the page.(`{% load static %}`)

> contact.html
```html
    <link rel="stylesheet" href="{% static 'CSS/index.csss' %}" />
```
