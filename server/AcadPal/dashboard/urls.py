from django.urls import path, re_path
from .views import *


urlpatterns = [
    path('', home_view, name='home'),
    re_path(r'^login/', login_user, name='student_signup'),
    re_path(r'^signup/student/', student_signup, name='student_signup'),
    re_path(r'^signup/teacher/', teacher_signup, name='student_signup'),
    ]
