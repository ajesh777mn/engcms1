from django.shortcuts import render
from adminapp.models import * #importing tables


# Create your views here.
def mcaintro(request):
    return render(request,'mca/mcaintro.html')

def mcaadmission(request):
    return render(request,'mca/mcaadmission.html')

def mcasyllabus(request):
    return render(request,'mca/mcasyllabus.html')

def mcaprequestions(request):
    return render(request,'mca/mcaprequestions.html')

def mcaextra(request):
    return render(request,'mca/mcaextra.html')

def mcafaculty(request):
    fac=faculty_mca.objects.all()
    return render(request,'mca/mcafaculty.html',{'fac':fac,})
def mca_faculties(request,id):
    data=faculty_mca.objects.get(id=id)
    return render(request,'mca/mca_faculties.html',{'data':data,})

def mca_eligibility(request):
    return render(request,'mca/mca_eligibility.html')

def darsanaramachandran(request):
    return render(request,'mca/darsanaramachandran.html')

def aryak(request):
    return render(request,'mca/aryak.html')
def testa(request):
    return render(request,'mca/testa.html')

    






