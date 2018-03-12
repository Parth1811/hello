from django.conf.urls import url
from . import views
from home_page.models import topics

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^1234/$', views.TEST1, name='TEST1'),
    url(r'^(?P<topics_id>[0-9]+)/$' ,views.test_topic, name = 'topic_test'),
    ]
