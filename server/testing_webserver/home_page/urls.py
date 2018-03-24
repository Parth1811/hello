from django.conf.urls import url
from . import views
from home_page.models import topics
from home_page.models import matsya_functions

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^1234/$', views.TEST1, name='TEST1'),
    url(r'^/topics/test_all/$',views.test_all_topics, name = 'all topics test'),
    url(r'^topics/(?P<topics_id>[0-9]+)/$' ,views.test_topic, \
        name = 'topic_test'),
    url(r'^functions/(?P<matsya_functions_id>[0-9]+)/$' ,\
        views.test_function, name = 'functions'),
    ]
