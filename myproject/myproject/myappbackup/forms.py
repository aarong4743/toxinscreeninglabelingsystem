# -*- coding: utf-8 -*-

from django import forms


#class DocumentForm(forms.Form):
#    docfile = forms.FileField(
#        label='Select a file'
#    )

class FileFieldForm(forms.Form):
    file_field = forms.FileField(label='Select a file',widget=forms.ClearableFileInput(attrs={'multiple': True}))

class IntegerFieldForm(forms.Form):
    num_eyes = forms.IntegerField(label='Number of Eyes')