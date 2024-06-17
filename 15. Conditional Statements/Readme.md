# What is If Else Statement in Django Template

```python
{% if numbers|length > 0 %}
        {% for n in numbers%}
            {% if n > 20 %}
            <div>{{n}}</div>
            {% endif %}
        {% endfor %}
    {% else %}
            <div>No Data Found</div>
    {% endif %}
```