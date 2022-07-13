
from html import escape
from io import BytesIO, StringIO
import re
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse


from eng import settings
from email.message import EmailMessage
from django.template.loader import get_template
# from xhtml2pdf import pisa 
# import pdfkit 

# from weasyprint import HTML
# import xhtml2pdf.pisa as pisa
# Create your views here.
from django.http import HttpResponse
from django.views.generic import View
from adminapp.models import * #importing tables

# from .process import html_to_pdf 


#Creating a class based view
# class GeneratePdf(View):
#     def get(self, request, *args, **kwargs):
         
#         # getting the template
#         pdf = html_to_pdf('online_appl.html')
         
#          # rendering the template
#         return HttpResponse(pdf, content_type='application/pdf')





def information_corner(request):
    data=informn_corner.objects.all()
    return render(request,'adminapp/information_corner.html',{'data':data,})
def info_corner(request,id):
    data=informn_corner.objects.get(id=id)
    return render(request,'adminapp/info_corner.html',{'data':data})  


def index(request):
    wp1=home_wallpaper.objects.get(id=1)
    wp2=home_wallpaper.objects.get(id=2)
    wp3=home_wallpaper.objects.get(id=3)
    wp4=home_wallpaper.objects.get(id=4)
    dept=departments.objects.all()
    exp_team=our_team.objects.all()
    news=news_updates.objects.all()
    notif=notifications.objects.all()

    
    return render(request,'adminapp/index.html',{'wp1':wp1,'wp2':wp2,'wp3':wp3,'wp4':wp4,'dept':dept,'exp_team':exp_team,'news':news,'notif':notif,})
def team(request,id):
        data=our_team.objects.get(id=id)
        return render(request,'adminapp/team.html',{'data':data})  

def course_intro(request,id):
    data=departments.objects.get(id=id)
    return render(request,'adminapp/course_intro.html',{'data':data})  

def profile(request):
    return render(request,'adminapp/profile.html')

def kvmtrust(request):
    return render(request,'adminapp/kvmtrust.html')

def libintroduction1(request):
    return render(request,'adminapp/libintroduction1.html')

def libfaculty(request):
    return render(request,'adminapp/libfaculty.html')

def courses(request):
    return render(request,'adminapp/courses.html')
def eligibility_criteria(request):
    return render(request,'adminapp/eligibility_criteria.html')
def scholarships(request):
    return render(request,'adminapp/scholarships.html')
def curricular(request):
    return render(request,'adminapp/curricular.html')  
def co_curricular(request):
    return render(request,'adminapp/co_curricular.html')  
   
def transportation(request):
    return render(request,'adminapp/transportation.html')  
def hostel(request):
    return render(request,'adminapp/hostel.html')  
def iedc(request):
    return render(request,'adminapp/iedc.html')  
def nature_club(request):
    return render(request,'adminapp/nature_club.html')
def placement(request):
    return render(request,'adminapp/placement.html')
def contact_us(request):
    return render(request,'adminapp/contact_us.html')
def approval_recognition(request):
    data=AICTE_latest_EOA.objects.get(id=1)
    eoa=AICTE_previous_EOA.objects.all()
    return render(request,'adminapp/approval_recognition.html',{'data':data,'eoa':eoa,})
def enquiry_form(request):
    data=application_form.objects.get(id=1)
    return render(request,'adminapp/enquiry_form.html',{'data':data,})
def brochures(request):
    data=brochure.objects.all()
    return render(request,'adminapp/brochures.html',{'data':data,}) 
def principal(request):
    return render(request,'adminapp/principal.html')

def Vision_Mission(request):
    return render(request,'adminapp/Vision_Mission.html')
def route_map(request):
    return render(request,'adminapp/route_map.html')
def photogallery(request):
    photos=photo_gallery.objects.all()
    return render(request,'adminapp/photogallery.html',{'photos':photos,})
def main_gallery(request,id):
        data=photo_gallery.objects.get(id=id)
        return render(request,'adminapp/main_gallery.html',{'data':data})  
def photos_international_workshop(request):
        return render(request,'adminapp/photos_international_workshop.html')
def photos_pseudocast(request):
    return render(request,'adminapp/photos_pseudocast.html')
def photos_placement_training(request):
    return render(request,'adminapp/photos_placement_training.html')
def photos_iedc(request):
    return render(request,'adminapp/photos_iedc.html')
def photos_arts_2017(request):
    return render(request,'adminapp/photos_arts_2017.html')
def photos_engclg(request):
    return render(request,'adminapp/photos_engclg.html')
def photos_sports(request):
    return render(request,'adminapp/photos_sports.html')
def event_list(request,id):
    data=latest_event.objects.get(id=id)
    return render(request,'adminapp/event_list.html',{'data':data,})
def photos_teloz_2k15(request):
    return render(request,'adminapp/photos_teloz_2k15.html')
def photos_lagori_rocks(request):
    return render(request,'adminapp/photos_lagori_rocks.html')
def photos_laboratories(request):
    return render(request,'adminapp/photos_laboratories.html')
def photos_infrastructure(request):
    return render(request,'adminapp/photos_infrastructure.html')
def photos_campus(request):
    return render(request,'adminapp/photos_campus.html')
def photos_mba(request):
    return render(request,'adminapp/photos_mba.html')
def photos_intelli(request):
    return render(request,'adminapp/photos_intelli.html')
def photos_IVmca(request):
    return render(request,'adminapp/photos_IVmca.html')


   
def events(request):
    data=latest_event.objects.all()
    return render(request,'adminapp/events.html',{'data':data,})
def national_seminar_potentials_biotechnology(request):
    return render(request,'adminapp/national-seminar-potentials-biotechnology.html')
def notice_board(request):
    notice=noticeboard.objects.all()
    return render(request,'adminapp/notice_board.html',{'notice':notice,})

def useful_links(request):
    links=useful_link.objects.all()
    return render(request,'adminapp/useful_links.html',{'links':links,})

def alumni(request):
    return render(request,'adminapp/alumni.html')
def media_update(request):
    media=media_updates.objects.all()
    return render(request,'adminapp/media_update.html',{'media':media})

def all_events(request):
    return render(request,'adminapp/all_events.html')

def news_events(request,id):
    data=news_updates.objects.get(id=id)
    return render(request,'adminapp/news_events.html',{'data':data})  

def seminar1(request):
    return render(request,'adminapp/seminar1.html')

def University_Guidelines(request):
    data=university_guidline.objects.all()
    return render(request,'adminapp/University_Guidelines.html',{'data':data,})

def notification(request,id):
    data=notifications.objects.get(id=id)
    return render(request,'adminapp/notification.html',{'data':data})  

def university_update(request):
    data=university_updates.objects.all()
    return render(request,'adminapp/university_update.html',{'data':data})
def mandatory_discl(request):
    data=mandatory_disclosure.objects.all()
    return render(request,'adminapp/mandatory_discl.html',{'data':data})




def online_appl(request):
    message=''
    if request.method=='POST':
        a=request.POST.get('fname')
        b=request.POST.get('mname')
        c=request.POST.get('lname')
        d=request.POST.get('gender')
        e=request.POST.get('dob')
        f=request.POST.get('religion')
        g=request.POST.get('caste')
		# nat=request.POST.get('nationality')
        i=request.POST.get('age')
        j=request.POST.get('marital_status')
        k=request.POST.get('blood_group')
        l=request.POST.get('applied_course')
        m=request.POST.get('qualify1')
        n=request.POST.get('institute1')
        o=request.POST.get('year1')
        p=request.POST.get('mark1')
        q=request.POST.get('qualify2')
        r=request.POST.get('institute2')
        s=request.POST.get('year2')
        t=request.POST.get('mark2')
        u=request.POST.get('qualify3')
        v=request.POST.get('institute3')
        w=request.POST.get('year3')
        x=request.POST.get('mark3')
        y=request.POST.get('qualify4')
        z=request.POST.get('institute4')
        ga=request.POST.get('year4')
        gb=request.POST.get('mark4')
        gc=request.POST.get('fathername')
        gd=request.POST.get('fatheroccupation')
        ge=request.POST.get('fatherincome')
        gf=request.POST.get('fatheraddress')
        gg=request.POST.get('fathertel')
        gh=request.POST.get('fathermobile')
        gi=request.POST.get('fatheremail')
        gj=request.POST.get('communication_address')
        gk=request.POST.get('declaration')

        if i!=0:

            template = get_template('adminapp/online_appl.html')
            context = {
                "fname": a,
                "age": i,
                "fathermobile": gh,
                "fatheremail": gi,
             }
            

            html  = template.render(context)
            result = BytesIO()
            pdf = pisa.pisaDocument(BytesIO(html.encode()), result, encoding="ISO-8859-1") #html.encode("ISO-8859-1")
            #pdf = pisa.pisaDocument(StringIO(html.encode("ISO-8859-1")), result)
            if not pdf.err:
                HttpResponse(result.getvalue(), content_type='application/pdf')
            else:
                HttpResponse('We had some errors<pre>%s</pre>' % escape(html))
            pdf = result.getvalue()
            filename = 'invoice.pdf'
            subject='online application form'
            emailfrom=settings.EMAIL_HOST_USER
            rlist=['ajeshmn.666@gmail.com']

            email = EmailMessage(subject, "helloji", emailfrom ,rlist)
            email.attach(filename, pdf, content_type = "application/pdf")
            email.send(fail_silently=False)

            message='registration done successfully'
        else:
            message='error occured'
    
    return render(request,'adminapp/online_appl.html',{'message':message})


def online_appl(request):
    message=''
    if request.method=='POST':
        a=request.POST.get('fname')
        b=request.POST.get('mname')
        c=request.POST.get('lname')
        d=request.POST.get('gender')
        e=request.POST.get('dob')
        f=request.POST.get('religion')
        g=request.POST.get('caste')
        i=request.POST.get('age')
        j=request.POST.get('marital_status')
        k=request.POST.get('blood_group')
        l=request.POST.get('applied_course')
        m=request.POST.get('qualify1')
        n=request.POST.get('institute1')
        o=request.POST.get('year1')
        p=request.POST.get('mark1')
        q=request.POST.get('qualify2')
        r=request.POST.get('institute2')
        s=request.POST.get('year2')
        t=request.POST.get('mark2')
        u=request.POST.get('qualify3')
        v=request.POST.get('institute3')
        w=request.POST.get('year3')
        x=request.POST.get('mark3')
        y=request.POST.get('qualify4')
        z=request.POST.get('institute4')
        ga=request.POST.get('year4')
        gb=request.POST.get('mark4')
        gc=request.POST.get('fathername')
        gd=request.POST.get('fatheroccupation')
        ge=request.POST.get('fatherincome')
        gf=request.POST.get('fatheraddress')
        gg=request.POST.get('fathertel')
        gh=request.POST.get('fathermobile')
        gi=request.POST.get('fatheremail')
        gj=request.POST.get('communication_address')
        gk=request.POST.get('declaration')
        if i!=0:
            import pdfcrowd
            import sys

            try:
    # create the API client instance
                client = pdfcrowd.HtmlToPdfClient('demo', 'ce544b6ea52a5621fb9d55f8b542d14d')

    # run the conversion and write the result to a file
                client.convertFileToFile('adminapp/templates/adminapp/online_appl.html', 'online_appl.pdf')
            except pdfcrowd.Error as why:
    # report the error
                sys.stderr.write('Pdfcrowd Error: {}\n'.format(why))

    # rethrow or handle the exception
                # raise

            # try:
    # create the API client instance
                # client = pdfcrowd.HtmlToPdfClient('demo', 'ce544b6ea52a5621fb9d55f8b542d14d')

    # run the conversion and write the result to a file
            #     client.convertUrlToFile('http://www.facebook.com', 'example.pdf')
            # except pdfcrowd.Error as why:
    # report the error
                # sys.stderr.write('Pdfcrowd Error: {}\n'.format(why))

    # rethrow or handle the exception
            # raise


            # pdfkit.from_file('geeksforgeeks.org','onlineForm.pdf')

    return render(request,'adminapp/online_appl.html')







# def display_laptops(request):
#     items = Laptops.objects.all()
#     context = {
#         'items': items,
#         'header': 'Laptops',
#     }
#     return render(request, 'adminapp/excell.html', context)


# def display_desktops(request):
#     items = Desktops.objects.all()
#     context = {
#         'items': items,
#         'header': 'Desktops',
#     }
#     return render(request, 'adminapp/excell.html', context)


# def display_mobiles(request):
#     items = Mobiles.objects.all()
#     context = {
#         'items': items,
#         'header': 'Mobiles',
#     }
#     return render(request, 'adminapp/excell.html', context)

# def excell(request):
#     return render(request,'adminapp/excell.html')


    


    

    
   


    
    
    
    
   
   
    










