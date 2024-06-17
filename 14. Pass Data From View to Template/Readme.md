# How to Pass Data From Django View to Template

Passing data from views to html.

> Views

```python
def homePage(request):
    data = {
        'title': 'HOME PAGE',
        'bdata' : 'Wecome to Homepage',
        'clist': ['PHP', 'JAVA' , 'DJANGO'],
        'student_details': [
            {'name': 'pradeep', 'phone' : 825203800},
            {'name': 'ayush', 'phone' : 82520380}
        ]
    }
    return render(request, "index.html" , data)
```

We have pass the data object to `index.html`

> index.html

```html
<h1>{{title}}</h1>
```

Used that variable in doble curly braces ` {{}}` to render.


## Django template for loop 

- `forloop.counter` - return current iteration of the loop (1-indexed)

- `forloop.counter0` - return current iteration of the loop (0-indexed)

- `forloop.revcounter` - The number of iterations from the end of the loop (1 - indexed)

- `forloop.revcounter0` - The number of iterations from the end of the loop (0 - indexed)

- `forloop.first` - Thrue if this is the fist time through the loop

- `forloop.last` - Thur if this i sthe last time through the loop

Displayed the data in views using for loop

> views.py
```python
def homePage(request):
    data = {
        'title': 'HOME PAGE',
        'bdata' : 'Wecome to Homepage',
        'clist': ['PHP', 'JAVA' , 'DJANGO'],
        'student_details': [
            {'name': 'pradeep', 'phone' : 825203800},
            {'name': 'ayush', 'phone' : 825203802}
        ]
    }
    return render(request, "index.html" , data)
```

> index.html

```html
 {% for n in clist %}
    <div>{{forloop.counter0}} {{n}}</div>
    {% endfor %}
    <br>
    <table border = "1" cellpadding='10'>
        <tr>
            <th>Name</th>
            <th>Phone no</th>
        </tr>

        {% for d in student_details%}
        <tr>
            <td>{{d.name}}</td>
            <td>{{d.phone}}</td>
        </tr>
        {% endfor %}
    </table>
```