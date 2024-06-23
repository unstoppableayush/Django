from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import usersForm
from django.core.mail import send_mail, EmailMultiAlternatives
import os
from django.conf import settings
from service.models import Service

def aboutus(request):
    return HttpResponse("Hello World")

def course(request):
    return HttpResponse("This is Course")
    
def courseDetails(request, courseid):
    return HttpResponse(courseid)

def homePage(request):
    data = {
        'title': 'HOME PAGE',
        'bdata' : 'Wecome to Homepage',
        'clist': ['PHP', 'JAVA' , 'DJANGO'],
        'numbers': [10, 20, 30, 40, 50],
        'student_details': [
            {'name': 'pradeep', 'phone' : 825203800},
            {'name': 'ayush', 'phone' : 825203802}
        ]
    }
    return render(request, "index.html" , data)

def about(request):
    if request.method=="GET":
        output=request.GET.get('output')
    return render(request, "about.html", {'output':output} )

def contact(request):
    return render(request, "contact.html")

def form(request):
    return render(request, "form.html")

def marksheet(request):
    if request.method == "POST":
        s1=eval(request.POST.get('subject1'))
        s2=eval(request.POST.get('subject2'))
        s3=eval(request.POST.get('subject3'))
        s4=eval(request.POST.get('subject4'))
        s5=eval(request.POST.get('subject5'))
        t=s1+s2+s3+s4+s5
        p=t*100/500
        if p>=60:
            d="First Div"
        elif p>=40:
            d="Second Div"
        elif p>=35:
            d="Third Div"
        else:
            d="Fail"
        #dicitonary
        data={
            'total':t,
            'per':p,
            'div':d
        }

        return render(request, "marksheet.html", data)
    return render(request, "marksheet.html")

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

def form(request):
    output = ""
    fm=usersForm()

    data={'form':fm}
    try:
        # fn = request.GET['fname'],
        # ln = request.GET['lname'],
        # em = request.GET.get('email')
        fn = request.POST['fname'],
        ln = request.POST['lname'],
        em = request.POST.get('email')
        output = str(fn)+str(ln)+str(em)
        data = {
            'form':fm,
            'output':output
        }

        url = "/about/?output={}".format
        return HttpResponseRedirect('/about', url)
    except:
        pass
    return render(request , 'form.html', data)

def submitform(request):
    try:
        if request.method=="POST":
            fn = request.POST.get('fname'),
            ln = request.POST.get('lname'),
            em = request.POST.get('email')
            output = str(fn)+str(ln)+str(em)

            return HttpResponse(output)
    except:
        pass

def sendmail(request):
    subject = 'Test Email'
    from_email = 'ayushkum884@gmail.com'
    msg  = '<h1>This is test email</h1>'
    to = ['ayushkum012@gmail.com']
    msg = EmailMultiAlternatives(subject, msg, from_email, to) 
    file_path = os.path.join(settings.BASE_DIR, 'Static/images/neuralink.jpg')
    print(file_path)
    msg.attach_file(file_path, 'image/jpg')
    msg.content_subtype='html'
    msg.send()
    # send_mail(
    #     'Testing Mail',
    #     'Here is the message',
    #     'ayushkum884@gmail.com',
    #     ['ayushkum012@gmail.com'],
    #     fail_silently=False
    # )
    return HttpResponse("Email Sent")

def services(request):
    services = Service.objects.all().order_by('-service_title')[:2]
    print(services)
    return render(request, 'services.html', {'services': services})