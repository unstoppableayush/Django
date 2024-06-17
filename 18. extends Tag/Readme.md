# Tags of Django | How to use Extends and Include Django Template Tags

We don't need to call header and footer on every pages.

This is why we make a base file which includes header and footer for all the files.

> base.html
```html
{% include "header.html" %}

{% block content  %}
{% endblock  %}

{% include "footer.html" %}
```

To use `base.html` in other pages.
> index.html

```html
{%  extends "base.html"  %}
{% block content %}
// body
{% endblock  %}
```