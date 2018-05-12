# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from channels import Group
from django.shortcuts import render

def index(request):
    Group("topic").send({
        "text": "this is from the views",
    })
    return render(request, 'chat/index.html')
