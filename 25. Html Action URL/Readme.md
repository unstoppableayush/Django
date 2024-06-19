# What is HTML Action URL in Django 

- By default it uses it's own page for redirection.

- It sends the data to other page uising `action` method.

- ` <form action="{% url "submitform" %}" method="post">`

- It will send the form data to submitform page.

- Created a data object and used it to pass the actual data into another page.

- Used the key in other page inside double curly braces to implement form

> views.py

```python
def form(request):
    output = ""
    fm=usersForm()

    data={'form':fm}
    try:
        # fn = request.GET['fname'],
        # ln = request.GET['lname'],
        # em = request.GET.get('email')
        fn = request.POST['fname'],
        ln = request.POST['lname'],
        em = request.POST.get('email')
        output = str(fn)+str(ln)+str(em)
        data = {
            'form':fm,
            'output':output
        }

        url = "/about/?output={}".format
        return HttpResponseRedirect('/about', url)
    except:
        pass
    return render(request , 'form.html', data)
```

> 