# Build a Calculator in Simple Ways in Django 

> urls.py
```python
 path('calculator/', views.calculator)
```

> views.py
```python
def calculator(request):
    c = ''
    try:
        if request.method=="POST":
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=request.POST.get('opr')
            if opr=="+":
                c=n1+n2
            elif opr=="-":
                c=n1-n2
            elif opr=="*" :
                c=n1*n2
            elif opr=="/":
                c=n1/n2
    except:
        c = "Invalid opr ..."
    print(c)
    return render(request, "calculator.html" , { 'c': c})
```

> calculator.html
```html
 <form action="" method="post">
        {% csrf_token %}
        <label for="">Value1</label>
        <input type="text" name="num1" >
        <label for="opr">Select OPR..</label>
        <select name="opr" >
            <option value="+">+</option>
            <option value="-">-</option>
            <option value="*">*</option>
            <option value="/">/</option>
        </select>
        <label for="">Value2</label>
        <input type="text" name="num2" >

        <button type="submit">Calculate</button>

        <br>
        <br>
        <label for="">Output</label>
        <br>
        <input value="{{c}}"" type="text">

    </form>
```