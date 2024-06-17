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
        'title': 'HOME PAGE'
    }
    return render(request, "index.html" , data)