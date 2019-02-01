from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from dashboard.models import User
from dashboard.forms import StudentSignUpForm, TeacherSignUpForm
from django.contrib.auth import authenticate, login

@login_required
def home_view(request):
    return render(request, "dashboard/home.html", {"name":request.user})

def login_user(request):
    if request.method == "GET":
        return render(request, "registration/login.html")
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
        return HttpResponseRedirect('/')
    else:
        print ("=-------IN HERE------------")
        # username = request.POST['username']
        # password = request.POST['password']
        print (request.__dict__.keys())
        print (request.resolver_match)
        # user = authenticate(username=username,password=password)
        # if user is not None:
        #     login(request, user)
        return HttpResponseRedirect('/')

def student_signup(request):
    if request.method == "GET":
        form = StudentSignUpForm()
        return render(request, "dashboard/test.html", {"form":form})
    if request.method == "POST":
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, "dashboard/test.html", {"form":form})

def teacher_signup(request):
    if request.method == "GET":
        form = TeacherSignUpForm()
        return render(request, "dashboard/test.html", {"form":form})
    if request.method == "POST":
        form = TeacherSignUpForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, "dashboard/test.html", {"form":form})
