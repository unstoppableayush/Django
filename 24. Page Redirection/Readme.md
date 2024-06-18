# What is Redirect and How to Redirect Page in Django

`from django.http import HttpResponseRedirect`

- We can use `HttpResponseRedirect` to redirect to other pages.

- We can also use `from django.shortcuts import redirect`  to redirect.

- We can also pass the value at the time of redirection. 

> views.py
```python
def form(request):
    output = ""
    try:
        # fn = request.GET['fname'],
        # ln = request.GET['lname'],
        # em = request.GET.get('email')
        fn = request.POST['fname'],
        ln = request.POST['lname'],
        em = request.POST.get('email')
        output = str(fn)+str(ln)+str(em)

        url = "/about/?output={}".format
        return HttpResponseRedirect('/about', url)
    except:
        pass
    return render(request , 'form.html', {'output':output})
```
- After form submission it will redirect to about page and will pass data in output

```python
def about(request):
    if request.method=="GET":
        output=request.GET.get('output')
    return render(request, "about.html", {'output':output} )
```

- about page will take output value and will pass to about page

> about.html
```html
 <p>Hello {{output}}</p>
```

- In about page the `output` value will be rendered.
