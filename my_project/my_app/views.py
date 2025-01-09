#my_app/views.py

import os
from django.http import HttpResponse
import json

def hello(request):
    return HttpResponse("Hello world!")

def ahoj(request):
    return HttpResponse("Ahoj světe!")

def articles(request):
    with open(os.path.join(os.path.dirname(__file__), 'articles.json')) as json_file:
        response_data = json.load(json_file)
    
    return HttpResponse(json.dumps(response_data), content_type="application/json")