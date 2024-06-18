from django.http import HttpResponse
from django.shortcuts import render
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
    return render(request, "about.html" )

def contact(request):
    return render(request, "contact.html")

def form(request):
    return render(request, "form.html")

def form(request):
    output = ""
    try:
        fn = request.GET['fname'],
        ln = request.GET['lname'],
        em = request.GET.get('email')
        output = fn
    except:
        pass
    return render(request , 'form.html', {'output':output})