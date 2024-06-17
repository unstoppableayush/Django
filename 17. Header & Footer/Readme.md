# Header and Footer in Django HTML Template (Fix Header & Footer)

We will try to implement one header and footer for all pages.

To include header and footer in other file we user `{% include "" %}`

```html
<body>
    {% include "header.html" %}
    <h1> About US</h1>
</body>
```