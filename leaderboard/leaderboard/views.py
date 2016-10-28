import json

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout, login

from social.backends.oauth import BaseOAuth1, BaseOAuth2
from social.backends.google import GooglePlusAuth
from social.backends.utils import load_backends
from social.apps.django_app.utils import psa

import odc as odc

def logout(request):
    """Logs out user"""
    auth_logout(request)
    return redirect('/')


@login_required(login_url="/login/google-oauth2/")
def uploadAFile(request):
    return render(request, "upload.html")


@login_required(login_url="/login/google-oauth2/")
def uploadedFile(request):
    fileUploaded = request.FILES['sentFile']
    # print type(fileUploaded)
    result = odc.score(False,'leaderboard/all_val_spend.csv',fileUploaded)
    # print odc.score(False,'all_val_spend.csv',fileUploaded)
    # return HttpResponse(fileUploaded)
    return render(
        request,
        'signup.html',
        {'displayContent': result}
        )

    # Handle file upload
    # if request.method == 'POST':
    #     form = DocumentForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         newdoc = Document(podId=request.POST['podId'],
    #                           location=request.POST['location'],
    #                           startDate=request.POST['startDate'],
    #                           endDate=request.POST['endDate'],
    #                           podUseType=request.POST['podUseType'],
    #                           pollutantOfInterest=request.POST['pollutantOfInterest'],
    #                           podUseReason=request.POST['podUseReason'],
    #                           docfile=request.FILES['docfile']
    #                          )
    #         newdoc.save()

    #         # Redirect to the document list after POST
    #         return HttpResponseRedirect(reverse('uploadedFiles'))
    # else:
    #     form = DocumentForm()  # A empty, unbound form
    # # Render list page with the documents and the form
    # return render(
    #     request,
    #     'upload.html',
    #     {'form': form}
    #     )
