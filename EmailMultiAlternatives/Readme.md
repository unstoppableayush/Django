# HTML Content and What is Email Multi Alternatives Function

# Sending Email in Django Project 

> views.py

`from django.core.mail import send_mail`

```python
def sendmail(request):
    subject = 'Test Email'
    from_email = 'ayushkum884@gmail.com'
    msg  = '<h1>This is test email</h1>'
    to = ['ayushkum012@gmail.com']
    msg = EmailMultiAlternatives(subject, msg, from_email, to) 
    msg.content_subtype='html'
    msg.send()
    return HttpResponse("Email Sent");
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