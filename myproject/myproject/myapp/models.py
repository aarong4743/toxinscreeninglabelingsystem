# -*- coding: utf-8 -*-
from django.db import models


class Document(models.Model):
	# the name of the file
	filename = models.CharField(default='me.txt',max_length=100)
	# this also represents the name of the file
	docfile = models.FileField(upload_to='documents/')
	# the number of eyes uploaded in the text box
	num_eyes = models.IntegerField(default=0)