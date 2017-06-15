# -*- coding: utf-8 -*-
from django.conf.urls import url
from myproject.myapp.views import FileFieldView
from myproject.myapp.views import onebyone
from myproject.myapp.views import welcome
from myproject.myapp.views import nameSet
from myproject.myapp.views import doWell
from myproject.myapp.views import tempClear

# list: Url for uploading documents. Must have set type and set name but can also have well id and num eyes
# onebyone: Url for iterating through worm images and inputting number of eyes. This is used for training sets only. Must be given set type (training), set name, image id, and previously entered number of eyes
# startlabeling: first worm label in training set. Must be given set type (training) and set name.
# welcome: Home page
# nameSet: name your training or test set. Must be given set type selected at welcome.
# firstWell: label your first well in the test set. Must be given set type (test) and set name.
# doWell: label your current well in the test set. Must be given set type (test), set name, well id, and previous number of eyes label. Has the option of taking done, which means that this is the last well.
# tempClear: clear documents in documents folder and model. Must be given set type (test), set name, well id, and previous number of eyes

urlpatterns = [
	url(r'^list/(?P<set_type>\w+)/(?P<set_name>\w+)$', FileFieldView.as_view(), name='list'),
    url(r'^list/(?P<set_type>\w+)/(?P<set_name>\w+)/(?P<well_id>\d+)/(?P<numbereyes>-?\d+)$', FileFieldView.as_view(), name='list'),
    url(r'^onebyone/(?P<set_type>\w+)/(?P<set_name>\w+)/(?P<image_id>\d+)/(?P<numbereyes>-?\d+)$', onebyone, name='onebyone'),
    url(r'^startlabeling/(?P<set_type>\w+)/(?P<set_name>\w+)$', onebyone, name='startlabeling'),
    url(r'^welcome/$', welcome, name='welcome'),
    url(r'^nameSet/(?P<set_type>\w+)$', nameSet, name='nameSet'),
    url(r'^firstWell/(?P<set_type>\w+)/(?P<set_name>\w+)$', doWell, name='doWell'),
    url(r'^doWell/(?P<set_type>\w+)/(?P<set_name>\w+)/(?P<well_id>\d+)/(?P<numbereyes>-?\d+)$', doWell, name='doWell'),
    url(r'^doWell/(?P<set_type>\w+)/(?P<set_name>\w+)/(?P<well_id>\d+)/(?P<numbereyes>-?\d+)/(?P<done>\d)$', doWell, name='doWell'),
    url(r'^tempClear/(?P<set_type>\w+)/(?P<set_name>\w+)/(?P<well_id>\d+)/(?P<numbereyes>-?\d+)$', tempClear, name='tempClear'),
]
