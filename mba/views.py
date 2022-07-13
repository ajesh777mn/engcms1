from django.shortcuts import render
from adminapp.models import * #importing tables


# Create your views here.
def mbaintro(request):
    return render(request,'mba/mbaintro.html')

def mbaadmission(request):
    return render(request,'mba/mbaadmission.html')

def mbabrochure(request):
    return render(request,'mba/mbabrochure.html')

def mbaambassodors(request):
    return render(request,'mba/mbaambassodors.html')

def mbafaculty(request):
    fac=faculty_mba.objects.all()
    return render(request,'mba/mbafaculty.html',{'fac':fac,})
def mba_faculties(request,id):
    data=faculty_mba.objects.get(id=id)
    return render(request,'mba/mba_faculties.html',{'data':data,})


def mba_eligibility(request):
    return render(request,'mba/mba_eligibility.html')
def drannkavithamathew(request):
    return render(request,'mba/drannkavithamathew.html')
def drvanoopkumar(request):
    return render(request,'mba/drvanoopkumar.html')
def drdeepakashokkumar(request):
    return render(request,'mba/drdeepakashokkumar.html')
# def arshavijay(request):
#     return render(request,'mba/arshavijay.html')
def akhils(request):
    return render(request,'mba/akhils.html')






