# FORM Tutorials in Django 

- Django can create forms through model.(admin)

- We can also create own from in frontside.

- First make a file `forms.py` imported the forms library.

- Created a class and pass the `forms.Form` and made the fields of input.

> forms.py
```python
class usersForm(forms.Form):
    fname=forms.CharField(
        label="First Name",
        required=False,
        widget=forms.TextInput(
            attrs={'class':"form-control"}
            ))
    lname=forms.CharField(label="Last Name",widget=forms.TextInput())
    email=forms.EmailField(label="Email")
```

- Imported `useFrom` using `from .forms import usersForm` in `views.py`.

- Called the class `useFrom` and stored in a variable.

> form.html

```python
<body>
    {% include "header.html" %}
    <form action="{% url "submitform" %}" method="post">
        {% csrf_token %}
        {% comment %} <label for="fname">First Name:</label>
        <input type="text" name="fname">
        <br>
        <label for="lname">Last Name:</label>
        <input type="text" name="lname">
        <br>
        <label for="email">Email:</label>
        <input type="email" name="email">
        <br>
        {% endcomment %}
        
        {{form}}

        <button type="submit" class="pt">Submit</button>
        <br>       
        <br>
        <input type="text" value= "{{output}}">
    </form>
    {% include "footer.html" %}
</body>
```