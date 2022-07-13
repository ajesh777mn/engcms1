from django.shortcuts import render
from adminapp.models import * #importing tables


# Create your views here.

def btechgovt(request):
    return render(request,'btech/btechgovt.html')
def engintroduction(request):
    return render(request,'btech/engintroduction.html')

def btechmgt(request):
    return render(request,'btech/btechmgt.html')

def btechnri(request):
    return render(request,'btech/btechnri.html')

def faculty(request):
    fac=faculty_btech.objects.all()
    return render(request,'btech/faculty.html',{'fac':fac,})
def btech_faculties(request,id):
    data=faculty_btech.objects.get(id=id)
    return render(request,'btech/btech_faculties.html',{'data':data,})

def keam2021onlinepreparation(request):
    return render(request,'btech/keam-2021-online-preparation.html')
def manjula_devanada(request):
    return render(request,'btech/manjula_devanada.html')
def minnukbenny(request):
    return render(request,'btech/minnukbenny.html')

