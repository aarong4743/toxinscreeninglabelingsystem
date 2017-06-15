# -*- coding: utf-8 -*-
from django.conf.urls import url
from myproject.myapp.views import FileFieldView
from myproject.myapp.views import onebyone

urlpatterns = [
    url(r'^list/$', FileFieldView.as_view(), name='list'),
    #url(r'^onebyone/(?P<image_id>\d+)/(?P<numbereyes>\d+)$', onebyone, name='onebyone'),
    url(r'^onebyone/(?P<image_id>\d+)/(?P<numbereyes>\d+)$', onebyone, name='onebyone'),
]
