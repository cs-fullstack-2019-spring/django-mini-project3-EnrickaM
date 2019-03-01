from django.shortcuts import render
from django.http import HttpResponse
from .models import TimeCard
from .forms import teachTimecardform

# Create your views here.
def index(request):
    return HttpResponse('Schools')

def all(request):
    allTimecards=''
    allEntries=TimeCard.objects.all()
    return render((request,'index.html',{'index':index}))
def create(request):
    form=teachTimecardform(request.POST or None)
    if form is valid():
        form.save()
        return redirect('all')

    return render((request,'teachTimecard-form.html',{'form':form}))

def update

