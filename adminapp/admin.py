from django.contrib import admin
from adminapp.models import *
# from import_export.admin import ImportExportModelAdmin


# Register your models here.
admin.site.register(notifications)
admin.site.register(home_wallpaper)
admin.site.register(departments)
admin.site.register(noticeboard)
admin.site.register(useful_link)
admin.site.register(our_team)
admin.site.register(faculty_btech)
admin.site.register(faculty_mba)
admin.site.register(faculty_mca)
admin.site.register(faculty_basicscience)
admin.site.register(photo_gallery)
admin.site.register(news_updates)
admin.site.register(media_updates)
admin.site.register(university_updates)
admin.site.register(university_guidline)
admin.site.register(mandatory_disclosure)
admin.site.register(latest_event)
admin.site.register(informn_corner)
admin.site.register(AICTE_latest_EOA)
admin.site.register(AICTE_previous_EOA)
admin.site.register(application_form)
admin.site.register(brochure)

# # Register your models here.

# # admin.site.register(item)
# @admin.register(Desktops, Laptops, Mobiles)
# class ViewAdmin(ImportExportModelAdmin):
#     exclude = ('id', )
