from django.http import HttpResponse

def aboutus(request):
    return HttpResponse("Hello World")

def course(request):
    return HttpResponse("This is Course")
    

