

> urls.py
```python
def evenodd(request):
    c=''
    try:
        if request.method=="POST":
            if  request.POST.get('num')=="":
                return render(request, "evenodd.html",{'error':True} )
            n=eval(request.POST.get('num'))
            if n%2 == 0 :
                c='Even'
            else:
                c='Odd'
    except:
        c="Enter valid no."
    
    return render(request, "evenodd.html", { 'c': c} )
```

> evenodd.html

```html
<form action="" method="post">
        {% if error %}
        <script>alert("Enter the value")</script>
        {% endif  %}
        
        {%  csrf_token %}
        <label for="">Value</label>
        <input type="text" name="num">
        
        <button type="submit">Even | Odd</button>
        <br>
        <br>
        <label for="">Output</label>
        <br>
        <input type="text" value="{{c}}">
    </form>
```