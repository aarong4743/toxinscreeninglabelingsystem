# -*- coding: utf-8 -*-

from django import forms

# this is used for collecting files before loading into Document model
class FileFieldForm(forms.Form):
    file_field = forms.FileField(label='Select a file',widget=forms.ClearableFileInput(attrs={'multiple': True}))

# I don't think this is used, but it can be used to collect the number of eyes you enter for the worm
class IntegerFieldForm(forms.Form):
    num_eyes = forms.IntegerField(label='Number of Eyes')