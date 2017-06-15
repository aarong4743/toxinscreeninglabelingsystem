# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from myproject.myapp.models import Document
#from myproject.myapp.forms import DocumentForm

from django.views.generic.edit import FormView
from myproject.myapp.forms import FileFieldForm

class FileFieldView(FormView):
    form_class = FileFieldForm
    template_name = 'list.html'  # Replace with your template.
    success_url = r'list/$'  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                newdoc = Document(docfile=f)
                newdoc.save()
        else:
            form = FileFieldForm()
        
         # Load documents for the list page
        documents = Document.objects.all()

        # Render list page with the documents and the form
        return render(
        request,
        'list.html',
        {'documents': documents, 'form': form}
        )

def onebyone(request, image_id, numbereyes):
    # Load only the necessary document
    documents_all = Document.objects.all()
    documents = documents_all[int(image_id)]
    print "image_id is: " + str(image_id)
    print "numbereyes is: " + str(numbereyes)
    #form_class = self.get_form_class()
    #form = self.get_form(form_class)
    #if form.is_valid():
    #    num_of_eyes = form.cleaned_data['num_eyes']
    #    documents.num_eyes = num_of_eyes
    #    documents.save()
    #else:
    #    form = IntegerFieldForm()
    # Render list page with the documents and the form
    return render(
    request,
    'onebyone.html',
    {'documents': documents, 'image_id': int(image_id), 'next' : (int(image_id) + 1)}
    )
