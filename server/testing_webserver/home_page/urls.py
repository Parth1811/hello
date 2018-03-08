from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^1234/$', views.TEST1, name='TEST1'),
    url(r'^t2/$', views.TEST2, name='TEST2'),
    ]
