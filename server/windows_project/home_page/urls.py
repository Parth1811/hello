from django.conf.urls import url
from django.urls import path
from . import views
from home_page.models import topics

urlpatterns = [
    path('', views.index, name='index'),
    path('1234/', views.TEST1, name='TEST1'),
    path('(?P<topics_id>[0-9]+)/' ,views.test_topic, name = 'topic_test'),
    ]
