# How to Pass Data From Django View to Template

Passing data from views to html.

> Views

```python
def homePage(request):
    data = {
        'title': 'HOME PAGE'
    }
    return render(request, "index.html" , data)
```

We have pass the data object to `index.html`

> index.html

```html
<h1>{{title}}</h1>
```

Used that variable in doble curly braces ` {{}}` to render.