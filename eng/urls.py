"""eng URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from adminapp.views import *
from btech.views import *
from mca.views import *
from mba.views import *
from basicscience.views import *
from django.urls import re_path
from django.conf.urls.static import static 



urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$',index,name='index'),
          re_path(r'^information_corner/$',information_corner,name='information_corner'),
         re_path(r'^info_corner/(?P<id>[0-9]+)',info_corner,name='info_corner'),

          
        re_path(r'^team/(?P<id>[0-9]+)',team,name='team'),

  
        re_path(r'^profile/$',profile,name='profile'),
        re_path(r'^kvmtrust/$',kvmtrust,name='kvmtrust'),
            re_path(r'^libintroduction1/$',libintroduction1,name='libintroduction1'),
            re_path(r'^libfaculty/$',libfaculty,name='libfaculty'),
            re_path(r'^course_intro/(?P<id>[0-9]+)',course_intro,name='course_intro'),
                re_path(r'^btechgovt/$',btechgovt,name='btechgovt'),
                re_path(r'^btechmgt/$',btechmgt,name='btechmgt'),
                re_path(r'^btechnri/$',btechnri,name='btechnri'),
                re_path(r'^faculty/$',faculty,name='faculty'),
                    re_path(r'^btech_faculties/(?P<id>[0-9]+)',btech_faculties,name='btech_faculties'),
                re_path(r'^engintroduction/$',engintroduction,name='engintroduction'),

                re_path(r'^manjula_devanada/$',manjula_devanada,name='manjula_devanada'),
                re_path(r'^minnukbenny/$',minnukbenny,name='minnukbenny'),
                re_path(r'^enquiry_form/$',enquiry_form,name='enquiry_form'),
                re_path(r'^brochures',brochures,name='brochures'),
                


                re_path(r'^mcaintro/$',mcaintro,name='mcaintro'),
                re_path(r'^mcaadmission/$',mcaadmission,name='mcaadmission'),
                re_path(r'^mcasyllabus/$',mcasyllabus,name='mcasyllabus'),
                re_path(r'^mcaprequestions/$',mcaprequestions,name='mcaprequestions'),
                re_path(r'^mcaextra/$',mcaextra,name='mcaextra'),
                re_path(r'^mcafaculty/$',mcafaculty,name='mcafaculty'),


                    re_path(r'^mbaintro/$',mbaintro,name='mbaintro'),
                    re_path(r'^mbaadmission/$',mbaadmission,name='mbaadmission'),
                    re_path(r'^mbabrochure/$',mbabrochure,name='mbabrochure'),
                    re_path(r'^mbaambassodors/$',mbaambassodors,name='mbaambassodors'),
                    re_path(r'^mbafaculty/$',mbafaculty,name='mbafaculty'),
                    re_path(r'^drannkavithamathew/$',drannkavithamathew,name='drannkavithamathew'),
                    re_path(r'^drvanoopkumar/$',drvanoopkumar,name='drvanoopkumar'),
                    re_path(r'^drdeepakashokkumar/$',drdeepakashokkumar,name='drdeepakashokkumar'),
                    re_path(r'^mba_faculties/(?P<id>[0-9]+)',mba_faculties,name='mba_faculties'),
                    re_path(r'^akhils/$',akhils,name='akhils'),



                    re_path(r'^basicintro/$',basicintro,name='basicintro'),
                    re_path(r'^basicfaculty/$',basicfaculty,name='basicfaculty'),

                    re_path(r'^courses/$',courses,name='courses'),
                    re_path(r'^eligibility_criteria/$',eligibility_criteria,name='eligibility_criteria'),
                    re_path(r'^mba_eligibility/$',mba_eligibility,name='mba_eligibility'),  
                    re_path(r'^mca_eligibility/$',mca_eligibility,name='mca_eligibility'),  
                    re_path(r'^scholarships/$',scholarships,name='scholarships'),  
                    re_path(r'^curricular/$',curricular,name='curricular'),  
                    re_path(r'^co_curricular/$',co_curricular,name='co_curricular'),
                    re_path(r'^transportation/$',transportation,name='transportation'),
                    re_path(r'^hostel/$',hostel,name='hostel'),
                    re_path(r'^iedc/$',iedc,name='iedc'),
                    re_path(r'^nature_club/$',nature_club,name='nature_club'),
                    re_path(r'^placement/$',placement,name='placement'),
                    re_path(r'^contact_us/$',contact_us,name='contact_us'),
                    re_path(r'^approval_recognition/$',approval_recognition,name='approval_recognition'),
                    re_path(r'^principal/$',principal,name='principal'),
                    re_path(r'^Vision_Mission/$',Vision_Mission,name='Vision_Mission'),
                    re_path(r'^route_map/$',route_map,name='route_map'),
                    
                    
                    re_path(r'^main_gallery/(?P<id>[0-9]+)',main_gallery,name='main_gallery'),
                    re_path(r'^photogallery/$',photogallery,name='photogallery'),
                    re_path(r'^photos_pseudocast/$',photos_pseudocast,name='photos_pseudocast'),
                    re_path(r'^photos_placement_training/$',photos_placement_training,name='photos_placement_training'),
                    re_path(r'^photos_iedc/$',photos_iedc,name='photos_iedc'),
                    re_path(r'^photos_arts_2017/$',photos_arts_2017,name='photos_arts_2017'),
                    re_path(r'^photos_engclg/$',photos_engclg,name='photos_engclg'),
                    re_path(r'^photos_sports/$',photos_sports,name='photos_sports'),
                    re_path(r'^photos_international_workshop/$',photos_international_workshop,name='photos_international_workshop'),
                    re_path(r'^photos_teloz_2k15/$',photos_teloz_2k15,name='photos_teloz_2k15'),
                    re_path(r'^photos_lagori_rocks/$',photos_lagori_rocks,name='photos_lagori_rocks'),
                    re_path(r'^photos_laboratories/$',photos_laboratories,name='photos_laboratories'),
                    re_path(r'^photos_infrastructure/$',photos_infrastructure,name='photos_infrastructure'),
                    re_path(r'^photos_campus/$',photos_campus,name='photos_campus'),
                    re_path(r'^photos_mba/$',photos_mba,name='photos_mba'),
                    re_path(r'^photos_intelli/$',photos_intelli,name='photos_intelli'),
                    re_path(r'^photos_IVmca/$',photos_IVmca,name='photos_IVmca'),

                    



                    re_path(r'^events/$',events,name='events'),
                    re_path(r'^keam-2021-online-preparation/$',keam2021onlinepreparation,name='keam-2021-online-preparation'),
                    re_path(r'^event_list/(?P<id>[0-9]+)',event_list,name='event_list'),

                    re_path(r'^notice_board/$',notice_board,name='notice_board'),
                    re_path(r'^useful_links/$',useful_links,name='useful_links'),
                    re_path(r'^alumni/$',alumni,name='alumni'),
                    re_path(r'^media_update/$',media_update,name='media_update'),
                    re_path(r'^University_Guidelines/$',University_Guidelines,name='University_Guidelines'),

        re_path(r'^all_events/$',all_events,name='all_events'),    
                             re_path(r'^news_events/(?P<id>[0-9]+)',news_events,name='news_events'),

        re_path(r'^seminar1/$',seminar1,name='seminar1'),

                    re_path(r'^university_update/$',university_update,name='university_update'),
                    re_path(r'^notification/(?P<id>[0-9]+)',notification,name='notification'),


                    

                    re_path(r'^darsanaramachandran/$',darsanaramachandran,name='darsanaramachandran'),
                    re_path(r'^mca_faculties/(?P<id>[0-9]+)',mca_faculties,name='mca_faculties'),
                    re_path(r'^basicscience_faculties/(?P<id>[0-9]+)',basicscience_faculties,name='basicscience_faculties'),
                    re_path(r'^testa/$',testa,name='testa'),
                            re_path(r'^online_appl/$',online_appl,name='online_appl'),
                            re_path(r'^mandatory_discl/$',mandatory_discl,name='mandatory_discl'),


#   re_path(r'^laptops$', display_laptops, name="display_laptops"),
#     re_path(r'^desktops$', display_desktops, name="display_desktops"),
#     re_path(r'^mobiles$', display_mobiles, name="display_mobiles"),
#     re_path(r'^excell$', excell, name="excell"),


]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
