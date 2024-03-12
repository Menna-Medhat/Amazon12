from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index1(request):
    return HttpResponse('<h1> سلام عليكم </h1>')
def index2(request):
    return HttpResponse('<h1>Hello World</h1>')
def index3(request, data):
    return HttpResponse(f' <h1 > Hi, {data}.</h1>')