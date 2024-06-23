# Sending Email in Django Project 

> views.py

`from django.core.mail import send_mail`

```python
def sendmail(request):
    send_mail(
        'Testing Mail',
        'Here is the message',
        'ayushkum884@gmail.com',
        ['ayushkum012@gmail.com'],
        fail_silently=False
    )
    return HttpResponse("Email Sent")
```


> settings.py

```python
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'ayushkum884@gmail.com'
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_TLS = True
```