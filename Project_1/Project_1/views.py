from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
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

def form(request):
    output = ""
    try:
        # fn = request.GET['fname'],
        # ln = request.GET['lname'],
        # em = request.GET.get('email')
        fn = request.POST['fname'],
        ln = request.POST['lname'],
        em = request.POST.get('email')
        output = str(fn)+str(ln)+str(em)

        url = "/about/?output={}".format
        return HttpResponseRedirect('/about', url)
    except:
        pass
    return render(request , 'form.html', {'output':output})

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