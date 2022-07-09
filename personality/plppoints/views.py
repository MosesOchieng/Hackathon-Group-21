from multiprocessing import context
from unittest import result
from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def home(request):
    return render(request,'home.html');

def points(request):
    if request.method=='POST':

        val=int(request.POST['points'])
        res=0
        if val==0:
            res=0
        if val==1:
            res=6
        if val==2:
            res=12
        if val==3:
            res=32
        if val>=4:
            res=60

        return render(request,"home.html",{"result": res})
    
    return render(request,"home.html")    
    


   