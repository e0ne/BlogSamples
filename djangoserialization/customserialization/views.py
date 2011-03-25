import json

from django.shortcuts import render_to_response
from django.core import serializers

from models import Employee, Person, Address
from serializer import to_json


def index(request):
    return render_to_response('index.html')

def default1(request):
    return render_to_response('default.html', {'data': serializers.serialize('json', Employee.objects.all())})

def default2(request):
    all_objects = list(Person.objects.all()) + list(Employee.objects.all()) + list(Address.objects.all() )
    data = serializers.serialize('json', all_objects)
    return render_to_response('default.html', {'data': data})

def custom1(request):
    return render_to_response('default.html', {'data': serializers.serialize('json', Person.objects.all(), indent=4, relations=('address',))})

def custom2(request):
    employees = []
    for employee in Employee.objects.all():
        employees.append(employee)
    data = json.dumps(employees, default=to_json)
    return render_to_response('default.html', {'data': data})