from django.shortcuts import render
from django.http import HttpResponse
import matplotlib.pyplot as plt


def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
    return render (request, 'home_page/home.html')

def TEST1(request):
    plt.plot([1,2,3,4,5,6,7,8,9])
    plt.show()
    return render (request, 'home_page/home.html')

