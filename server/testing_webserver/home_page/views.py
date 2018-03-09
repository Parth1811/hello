from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import checker
import rospy

def index(request):
#    return HttpResponse("Hello, world. You're at the polls index.")
    return render (request, 'home_page/home.html')

def TEST1(request):
#    rospy.init_node('checker', anonymous=True)
    ch = checker.Checker()
    status_map = ch.run2()
    print (status_map)
    return HttpResponseRedirect('../')

def TEST2(request):
    ch = checker.Checker(10) ## 3 seconds
    running = ch.run()
    print("************ running:", running)
    return HttpResponseRedirect('../')
