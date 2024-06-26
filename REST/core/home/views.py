from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.serializers import PeopleSerializer
from .models import Person

@api_view(['GET','POST', 'PUT'])
def index(request):
    courses = {
            'course_name': 'Python Programming',
            'learn': ['flask', 'Django', 'Python', 'Fastapi', 'Tornado'],
            'course_provider': 'Scaler'
        }
    if request.method == 'GET':
        print("///")
        print(request.GET.get('search'))
        print("///")
        print("YOU HIT A GET METHOD")
        return Response(courses)
    elif request.method=='POST':
        data = request.data
        print('****')
        print(data)
        print(data['name'])
        print('****')
        print('YOU HIT A POST METHOD')
        return Response(courses )
    elif request.method == 'PUT':
        print('YOU HIT A POST METHOD')
        return Response(courses)

@api_view(['GET','POST','PUT', 'PATCH', 'DELETE'])
def person(request):
    if request.method == "GET" :
        objs = Person.objects.all()
        serializer = PeopleSerializer(objs, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = PeopleSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method == 'PUT':
        data = request.data
        object = Person.objects.get(id = data['id']) 
        serializer = PeopleSerializer(object , data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    # supports partial update 
    elif request.method == 'PATCH':
        data = request.data                           # getting data from request
        object = Person.objects.get(id = data['id'])  # extracting the data having same id
        serializer = PeopleSerializer(object , data = data, partial = True) 
        # passing object and new data and also partial update should be true

        if serializer.is_valid():                    # validating the serializer
            serializer.save()                        # if valid then save
            return Response(serializer.data)         # and return the saved response
        return Response(serializer.errors)

    else:
        data = request.data
        obj = Person.objects.get(id = data['id'])
        obj.delete()
        return Response({'message': 'Person deleted'})