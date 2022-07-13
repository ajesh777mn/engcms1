from django.shortcuts import render
from adminapp.models import * #importing tables


# Create your views here.
def basicfaculty(request):
    fac=faculty_basicscience.objects.all()
    return render(request,'basicscience/basicfaculty.html',{'fac':fac,})
def basicscience_faculties(request,id):
    data=faculty_basicscience.objects.get(id=id)
    return render(request,'basicscience/basicscience_faculties.html',{'data':data,})


def basicintro(request):
    return render(request,'basicscience/basicintro.html')

def aryak(request):
    return render(request,'basicscience/aryak.html')
