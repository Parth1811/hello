import matplotlib.pyplot as plt
import threading

from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages

from auv_state import matsya
import checker
from home_page.models import matsya_functions
from home_page.models import topics
from matsya_wrapper import get_battery_percent
from matsya_wrapper import run_function

class_obj = matsya.Matsya()

def test_thread_helper(request, data):
    ch = checker.Checker(data.title, data.topic_name, data.ros_msg_type,\
        data.max_post_required, data.timeout)
    status = ch.run()
    if (status):
        messages.success(request, data.title + ' is Working :)')
    else:
        messages.warning(request, data.title + ' is NOT Workinig :(')

def index(request):
    data_transfer = dict()
    data_transfer['topic_list'] = topics.objects.all()
    data_transfer['function_list'] = matsya_functions.objects.all()
    data_transfer['battery_status'] = get_battery_percent(class_obj)
    print (data_transfer['topic_list'])
    return render (request, 'home_page/home.html',data_transfer)

def TEST1(request):
    if run_function('actuateGripper'):
        messages.success(request, ' is Working :)')
    else:
        messages.success(request, ' is NOt Working :)')
    return HttpResponseRedirect('../../')

def test_topic(request,topics_id):
    indata = topics.objects.get(id = topics_id)
    test_thread_helper(request, indata)
    return HttpResponseRedirect('../../')


def test_all_topics(request):
    indata = topics.objects.all()
    thread_map = dict()
    for data in indata:
        thread_map[data.title] = threading.Thread(target = test_thread_helper,\
            args=[request, data])
        thread_map[data.title].start()

    for thread in thread_map:
        thread_map[thread].join()

    return HttpResponseRedirect('../../')

def test_function(request,matsya_functions_id):
    indata = matsya_functions.objects.get(id = matsya_functions_id)
    if run_function(indata.function_name):
        messages.success(request, ' is Working :)')
    else:
        messages.success(request, ' is NOt Working :)')
    return HttpResponseRedirect('../../')

