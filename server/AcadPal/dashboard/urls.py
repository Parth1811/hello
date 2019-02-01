from django.urls import path, re_path, include
from rest_framework import routers

from .views import *
from .api_views import *

router = routers.DefaultRouter()
router.register(r'student', StudentViewSet)

urlpatterns = [
    path('', home_view, name='home'),
    re_path(r'^router/', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^login/', login_user, name='student_signup'),
    re_path(r'^signup/student/', student_signup, name='student_signup'),
    re_path(r'^signup/teacher/', teacher_signup, name='student_signup'),
    ]
