from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import matplotlib.pyplot as plt
import checker
from home_page.models import topics

def index(request):
    data_transfer = dict()
    data_transfer['topic_list'] = topics.objects.all()
    print (data_transfer['topic_list'])
    return render (request, 'home_page/home.html',data_transfer)

def TEST1(request):
    ch = checker.Checker()
    data = ch.run()
    print ("======================")
    print (data)
    print ("======================")
    return HttpResponseRedirect('../')

def test_topic(request,topics_id):
    req_data = topics.objects.get(id = topics_id)
    ch = checker.Checker(req_data.title,req_data.topic_name, req_data.ros_msg_type)
    data = ch.run()
    print ("======================")
    print (data)
    print (topics_id)
    print ("======================")
    return HttpResponseRedirect('../')

