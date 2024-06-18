# Implement GET Method Form in Django

> views.py
```python
def form(request):
    try:
        fn = request.GET['fname'],
        ln = request.GET['lname'],
        em = request.GET.get('email')
        print(fn+ln+em)
    except:
        pass
    return render(request , 'form.html')
```

> form.html

```html
<form action="" method="get">
        <label for="fname">First Name:</label>
        <input type="text" name="fname">
        <br>
        <label for="lname">Last Name:</label>
        <input type="text" name="lname">
        <br>
        <label for="email">Email:</label>
        <input type="email" name="email">
        <br>
        <button type="submit" class="pt">Submit</button>
    </form>
```

-  You can change the data from url.