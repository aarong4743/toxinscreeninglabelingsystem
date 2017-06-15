# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db import models

from myproject.myapp.models import Document

from django.views.generic.edit import FormView
from myproject.myapp.forms import FileFieldForm

import cv2
import os
import glob


class FileFieldView(FormView):
    form_class = FileFieldForm
    template_name = 'list.html'  # Replace with your template.
    success_url = r'list/$'  # Replace with your URL or reverse().

    # this method runs when upload button is clicked
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        # if form is valid, add create instance of Document model for all files
        if form.is_valid():
            for f in files:
                newdoc = Document(filename=f, docfile=f)
                newdoc.save()
        else:
            form = FileFieldForm()
        
         # Load documents for the list page
        documents = Document.objects.all()

        num_images = len(documents)

        # Render list page with the documents and the form
        return render(
        request,
        'list.html',
        {'documents': documents, 'form': form, 'num_images': num_images}
        )

# method runs for labeling all images in training set
def onebyone(request, set_type, set_name, image_id="0", numbereyes="0"):

    # if this is the first image, set up all necessary directories
    if (int(image_id) == 0):
        os.makedirs("media/" + set_type + '/' + set_name)
        os.makedirs("media/" + set_type + '/' + set_name + "/0_Eyes")
        os.makedirs("media/" + set_type + '/' + set_name + "/1_Eye")
        os.makedirs("media/" + set_type + '/' + set_name + "/2_Eyes")
        os.makedirs("media/" + set_type + '/' + set_name + "/Weird")

    # load all documents
    documents_all = Document.objects.all()
    # if this is not past the last document, get current one from array
    if (int(image_id) != len(documents_all)):
        document_send = documents_all[int(image_id)]
    print "image_id is: " + str(image_id)
    print "numbereyes is: " + str(numbereyes)
    
    # if this is not the first image, update previous one by copying it into proper folder based on the number of eyes it was labeled as. Also update its num_eyes field.
    if int(image_id) != 0:
        document_update = documents_all[int(image_id)-1]
        document_update.num_eyes = int(numbereyes)
        cpimg = cv2.imread("media/documents/" + document_update.filename)
        if int(numbereyes) == 0:
            cv2.imwrite("media/" + set_type + '/' + set_name + "/0_Eyes/" + document_update.filename, cpimg)
        if int(numbereyes) == 1:
            cv2.imwrite("media/" + set_type + '/' + set_name + "/1_Eye/" + document_update.filename, cpimg)
        if int(numbereyes) == 2:
            cv2.imwrite("media/" + set_type + '/' + set_name + "/2_Eyes/" + document_update.filename, cpimg)
        if int(numbereyes) == -1:
            cv2.imwrite("media/" + set_type + '/' + set_name + "/Weird/" + document_update.filename, cpimg)
        document_update.save()

    # if this is past the last document, render endLabeling page
    if (int(image_id) == len(documents_all)):
        return render(request, 'endlabeling.html')
    
    # render documents, current image id, next image id, training as set type, and set name
    return render(
    request,
    'onebyone.html',
    {'documents': document_send, 'image_id': int(image_id), 'next' : (int(image_id) + 1), 'set_type': set_type, 'set_name': set_name}
    )

# this method is run as the home page
def welcome(request):
    # clear all instances of Document object
    documents = Document.objects.all()
    for i in range(0,len(documents)):
        documents[i].delete()
    # clear all files in documents folder
    files = glob.glob('media/documents/*.jpeg')
    for f in files:
        os.remove(f)
    return render(request, 'welcome.html')

# method run for naming set
def nameSet(request, set_type):
    return render(request, 'nameSet.html', {'set_type': set_type})

# method run for labeling each well
def doWell(request, set_type, set_name, well_id="1", numbereyes="0", done="0"):
    # if this is the first well, set up all directories
    if (int(well_id) == 1):
        os.makedirs("media/" + set_type + '/' + set_name)
        os.makedirs("media/" + set_type + '/' + set_name + '/tempWell')
        os.makedirs("media/" + set_type + '/' + set_name + "/0_Eyes")
        os.makedirs("media/" + set_type + '/' + set_name + "/1_Eye")
        os.makedirs("media/" + set_type + '/' + set_name + "/2_Eyes")
        os.makedirs("media/" + set_type + '/' + set_name + "/Weird")

    print "well_id is: " + str(well_id)
    print "numbereyes is: " + str(numbereyes)

    # if this is not the first well, make directory for storing well images
    if int(well_id) != 1:
        if int(numbereyes) == 0:
            os.makedirs("media/" + set_type + '/' + set_name + "/0_Eyes/" + str(int(well_id)-1))
        if int(numbereyes) == 1:
            os.makedirs("media/" + set_type + '/' + set_name + "/1_Eye/" + str(int(well_id)-1))
        if int(numbereyes) == 2:
            os.makedirs("media/" + set_type + '/' + set_name + "/2_Eyes/" + str(int(well_id)-1))
        if int(numbereyes) == -1:
            os.makedirs("media/" + set_type + '/' + set_name + "/Weird/" + str(int(well_id)-1))

        # collect all images from tempWell folder and move into folder with correct label
        images = []
        for img in glob.glob("media/" + set_type + '/' + set_name + '/tempWell/*.jpeg'):
            images.append(img)
        for a in range(0,len(images)):
            cpimg = cv2.imread("media/" + set_type + '/' + set_name + '/tempWell/' + images[a][images[a].rindex("/")+1:],0)
            if int(numbereyes) == 0:
                cv2.imwrite("media/" + set_type + '/' + set_name + "/0_Eyes/" + str(int(well_id)-1) + '/' + images[a][images[a].rindex("/")+1:], cpimg)
            if int(numbereyes) == 1:
                cv2.imwrite("media/" + set_type + '/' + set_name + "/1_Eye/" + str(int(well_id)-1) + '/' + images[a][images[a].rindex("/")+1:], cpimg)
            if int(numbereyes) == 2:
                cv2.imwrite("media/" + set_type + '/' + set_name + "/2_Eyes/" + str(int(well_id)-1) + '/' + images[a][images[a].rindex("/")+1:], cpimg)
            if int(numbereyes) == -1:
                cv2.imwrite("media/" + set_type + '/' + set_name + "/Weird/" + str(int(well_id)-1) + '/' + images[a][images[a].rindex("/")+1:], cpimg)

    # remove all files in tempWell folder
    files = glob.glob("media/" + set_type + '/' + set_name + '/tempWell/*.jpeg')
    for f in files:
        os.remove(f)

    # if this is not the last well, copy images from documents folder into tempWell folder
    if (int(done) != 1):
        images = []
        for img in glob.glob("media/documents/*.jpeg"):
            images.append(img)
        for a in range(0,len(images)):
            cpimg = cv2.imread("media/documents/" + images[a][images[a].rindex("/")+1:],0)
            cv2.imwrite("media/" + set_type + '/' + set_name + "/tempWell/" + images[a][images[a].rindex("/")+1:], cpimg)

    # retrieve all documents
    documents_all = Document.objects.all()

    # if we are finished labeling, render lastWell page
    if (int(done) == 1):
        return render(request, 'lastWell.html')

    # render documents, well id, next well id, set type (test), and set name
    return render(
    request,
    'doWell.html',
    {'documents': documents_all, 'well_id': int(well_id), 'next' : (int(well_id) + 1), 'set_type': set_type, 'set_name': set_name}
    )

# method for clearing all Document object instances and documents folder
def tempClear(request, set_type, set_name, well_id, numbereyes):
    # clear all document instances
    documents = Document.objects.all()
    for i in range(0,len(documents)):
        documents[i].delete()
    # clear everything in documents folder
    files = glob.glob('media/documents/*')
    for f in files:
        os.remove(f)
    return render(request, 'tempClear.html')
