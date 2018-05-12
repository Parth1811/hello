from django.shortcuts import render
from django.http import HttpResponse
import reader_helper

def index(request):
   #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'ros_reader/index.html', {})
