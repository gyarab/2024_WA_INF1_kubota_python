from django.shortcuts import render
from django.http import HttpResponse as HTTPResponse

# Create your views here.
def hello_world(request):
    return HTTPResponse('Hello World')