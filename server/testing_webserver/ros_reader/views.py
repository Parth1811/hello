from django.shortcuts import render
from django.http import HttpResponse
import reader_helper

def index(request):
    ch = reader_helper.Checker('dvl','/dvl/data','DvlData')
    status = 11111111
    ch.msg_read()
    while True:
        msg = ch.get_data()
        null = []
        if msg != null:
            print msg
    print status
    return HttpResponse("Hello, world. You're at the polls index.")

