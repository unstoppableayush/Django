# Creating a Dynamic URL in Django

Dynamic Url can take three values:

1. int
2. str
3. slug

>views.py
```python
def courseDetails(request, courseid):
    return HttpResponse(courseid)
```

>urls.py
```python
    #int
    path('course/<int:courseid>',views.courseDetails)
    
    #string
    path('course/<str:courseid>',views.courseDetails)

    #slug
    path('course/<slug:courseid>',views.courseDetails)

    #don't know any type 
    path('course/<courseid>',views.courseDetails)
```