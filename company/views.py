from django.shortcuts import render
from .forms import *
from .models import *
from django.shortcuts import*
from django.http import*
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request,'index.html')
def about(request):
    return render(request,'hy.html')
def kitchen(request):
    return render(request,'kitchen.html')
def query(request):
    if request.method=="POST":
        form = index_form(request.POST)
        print (request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            print (cd)

            send_mail('Inquiry' , 'Your Query Has been sent to Our Design ! Thanks .' ,'our design', [cd['email']])
            send_mail('Inquiry' , 'you have a new query :' [cd['inquiry']]  ,[cd['email']], 'gmuskan408@gmail.com')
            form.save()
            return HttpResponseRedirect('/')

    else:
        form = index_form()
    return render(request,'query.html',{'form':form})

def space(request):
    return render(request,'space.html')
def index(request):
    return render(request,'index1.html')
def res(request):
    return render(request,'res.html')
def gallery(request):
        return render(request,'gall.html')
def bathroom(request):
    return render(request,'bathroom.html')
def appointment(request):
    if request.method=="POST":
        form = appoint_form(request.POST)
        print (request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            print (cd)


            form.save()
            return HttpResponseRedirect('/')

    else:
        form = index_form()
    return render(request,'appointment.html')
