from typing import ContextManager
from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
import random 
import smtplib 

# Create your views here.

def index(request):
    return render(request, 'index.html')

def mathpalace(request):
    return render(request, 'mathpalace.html')

def networkingmain(request):
    return render(request, 'networkingmain.html')

def networkingProjects(request):
    context = {}

    context['string_list'] = parseNetworkingProjects()
   
    return render(request, 'networkingProjects.html', context)

def networkingNotes(request):
    context = {}

    context['string_list'] = parseNetworkingTextNotes()

    return render(request, 'networkingNotes.html', context)

def arithmeticpalace(request):

    return render(request, 'arithmeticpalace.html')

def parseNetworkingProjects():
    file = open("/home/taylor/Desktop/everything/NetworkingProjects.txt", "r")

    lines = file.readlines() 
    
    hold = []

    for line in lines:
       global num
       num = line
       hold.append(num)

    return hold        

def parseArithmeticText():
    
    file = open("/ArthmeticNotes.txt", "r")

    lines = file.readlines() 
    
    hold = []

    for line in lines:
       global num
       num = line.split('&')
       hold.append(num[0])

    return hold        

def parseNetworkingTextNotes():
    file = open("/home/taylor/Desktop/everything/NetworkingNotes.txt", "r")

    lines = file.readlines() 
    
    hold = []

    for line in lines:
       global num
       num = line
       hold.append(num)

    return hold        

   


