from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from resthome.models import Person
from resthome.serializers import PersonSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


@api_view(['GET'])
def get_persons(request):
    persons = Person.objects.all()
    serializer = PersonSerializer(persons, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_person(request):
    serializer = PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
def update_person(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response({'error': 'Person not found'}, status=404)

    serializer = PersonSerializer(person, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_person(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response({'error': 'Person not found'}, status=404)

    person.delete()
    return Response({'profile is deleted!'},status=204)




    # @api_view(['GET','POST','PUT','PATCH','DELETE'])
    # def person(request):
    #     if request.method == 'GET':
    #         objPerson = Person.objects.all()
    #         serializer = PersonSerializer(objPerson, many = True)
    #         return Response(serializer.data)
    #     elif request.method == 'POST':
    #         data = request.data
    #         serializer = PersonSerializer(data = data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data)
    #         return Response(serializer.errors)
    #     elif request.method == 'PUT':
    #         data = request.data
    #         obj = Person.objects.get(id = data['id'])
    #         serializer = PersonSerializer(obj, data = data, partial = False)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data)
    #         return Response(serializer.errors)
    #     elif request.method == 'PATCH':
    #         data = request.data
    #         obj = Person.objects.get(id = data['id'])
    #         serializer = PersonSerializer(obj, data = data, partial = True)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return Response(serializer.data)
    #         return Response(serializer.errors)
    #     else:
    #         data = request.data
    #         obj = Person.objects.get(id = data['id'])
    #         obj.delete()
    #         return Response({'message': 'Person deleted'})    