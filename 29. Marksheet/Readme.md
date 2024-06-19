# Create Marksheet in Simple ways in Django

> urls.py
```python
 path('marksheet', views.marksheet)
```

> marksheet.html
```html

<form action="" method="post">
        {% csrf_token %}
        <label for="">Subject1</label>
        <input type="text" name="subject1">
        <br>
        <label for="">Subject2</label>
        <input type="text" name="subject2">
        <br>
        <label for="">Subject3</label>
        <input type="text" name="subject3">
        <br>
        <label for="">Subject4</label>
        <input type="text" name="subject4">
        <br>
        <label for="">Subject5</label>
        <input type="text" name="subject5">
        <br>
        <button type="submit">Marksheet</button>
        <br>
        <br>
        <label for="">Total</label>
        <input type="text" value="{{total}}">
        <br>
        <label for="">Percentes</label>
        <input type="text" value="{{per}}">
        <br>
        <label for="">Divison</label>
        <input type="text" value="{{div}}">
    </form>
```

> views.py
```python
def marksheet(request):
    if request.method == "POST":
        s1=eval(request.POST.get('subject1'))
        s2=eval(request.POST.get('subject2'))
        s3=eval(request.POST.get('subject3'))
        s4=eval(request.POST.get('subject4'))
        s5=eval(request.POST.get('subject5'))
        t=s1+s2+s3+s4+s5
        p=t*100/500
        if p>=60:
            d="First Div"
        elif p>=40:
            d="Second Div"
        elif p>=35:
            d="Third Div"
        else:
            d="Fail"
        #dicitonary
        data={
            'total':t,
            'per':p,
            'div':d
        }

        return render(request, "marksheet.html", data)
    return render(request, "marksheet.html")
```