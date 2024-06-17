# How to Render an HTML Template as Response 

To use templates folder file `'DIRS': [BASE_DIR, "Templates"],` chnages the `DIRS` in settings.py

To render html file use `from django.shortcuts import render` in `views.py`

> views.py

```python

def homePage(request):
    return render(request, "index.html")

```
> urls.py

```python
path('',views.homePage),
```