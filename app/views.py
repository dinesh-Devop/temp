from json.encoder import JSONEncoder
import math
from turtle import heading
from typing import Counter

from django.db.models.fields import PositiveIntegerField
from app.forms import CsvModelForm,txtform
import logging
import unicodedata,twint,os,pandas as pd
from django.http.response import HttpResponseRedirect
from six import b
import requests,json,random,datetime
from background_task import background
from bs4 import BeautifulSoup
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from app.models import *
from django.contrib import messages

from django.contrib.auth import authenticate, get_user_model
from datetime import date
from django.contrib.auth.hashers import make_password
from django.shortcuts import render

from django.core.mail import send_mail
from django.core.validators import validate_email
from django import forms


#Webpage functions


def oragnizerLogin(request):

        if request.method == 'POST':
            
            name2 = request.POST.get('bname')
            heading = request.POST.get('heading')
            subject = request.POST.get('subject')
            details = request.POST.get('Details')
           
            photo = request.POST.get('photo')
            print(name2,details,photo)
         
            Admins.objects.create(name=name2,title=heading,article=details,photolink=photo,subject=subject)
            return redirect('/blog')
           
            
            
        else:
            return render(request, 'login.html')

def blogs(request):
    v=Admins.objects.all()
    name=[]
    title=[]
    details=[]
    image=[]
    id=[]
    subject=[]
    for i in range(len(v)):
        name.append(v[i].name)
        title.append(v[i].title)
        details.append(v[i].article)
        image.append(v[i].photolink)
        id.append(v[i].id)
        subject.append(v[i].subject)

    context={'name':name,'title':title,'details':details,'image':image,'id':id,'subject':subject}
    return render(request,'index1.html',context)

def index(request):
    v=Admins.objects.all()
    return render(request, 'inder.html')

# def admin(request):
#     v=Admins.objects.all()
#     return render(request, 'login.html')


def vg(request):
    v=Admins.objects.all()
    return render(request, 'single-standard.html')

def blogroute(request,id):
   
    
    v=Admins.objects.get(id=id)
    name=v.name
    title=v.title
    details=v.article
    image=v.photolink
    i=int(id)
    

    context={'name':name,'title':title,'details':details,'image':image,'id':i}

    return render(request, 'single-standard.html',context)
 
