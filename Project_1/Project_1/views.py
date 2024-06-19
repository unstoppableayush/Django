from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import usersForm

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