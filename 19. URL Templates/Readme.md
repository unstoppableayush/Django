# What are URL Template Tags in Django and How to Use It

To manage urls

> Using Anchor Tag

for home - href="/",
for contact - href="/contact"

> Using URLS Tag

Here we are providing name using that name we can distinguised the specific url.
> urls.py
```pyhton
path('about/',views.about, name="about"),
path('',views.homePage, name="home"),
path('contact/',views.contact, name="contact"),
```

> index.html

```html
  <h2>URLs using Url Tag</h2>
    <a href="{% url "home" %}">Home</a>
    <a href="{% url "contact" %}">Contact</a>
    <a href="{% url "about" %}">About</a>
```