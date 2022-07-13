from turtle import heading
from django.db import models

# Create your models here.
class notifications(models.Model):
    marquee_text=models.CharField(max_length=300)
    photo=models.ImageField(upload_to='img',verbose_name='file',null=True,blank=True,default='-')
    post_date=models.CharField(max_length=50)
    title=models.CharField(max_length=150)
    details=models.TextField()


class home_wallpaper(models.Model):
    wallpaper_text=models.CharField(max_length=150)
    wallpaper_pic=models.ImageField(upload_to='img',verbose_name='file',null=True,blank=True,default='-')
    
class departments(models.Model):
    dept_name=models.CharField(max_length=150)
    pic=models.ImageField(upload_to='img',verbose_name='file',null=True,blank=True,default='-')

    course_name=models.CharField(max_length=200)
    duration=models.CharField(max_length=100)
    intake=models.CharField(max_length=100)
    description1=models.CharField(max_length=500)
    description2=models.CharField(max_length=500)
    description3=models.CharField(max_length=500)
    description4=models.CharField(max_length=500)


class noticeboard(models.Model):
    pdf = models.FileField()
    heading=models.CharField(max_length=200)
class useful_link(models.Model):
    heading=models.CharField(max_length=200)
    website_link=models.CharField(max_length=200)
class our_team(models.Model):
    photo=models.ImageField(upload_to='img',verbose_name='file',null=True,blank=True,default='-')
    name=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)
    dateOf_join=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    designation=models.CharField(max_length=150)
    department=models.CharField(max_length=50)
    experience=models.CharField(max_length=50)
    dateOf_join=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    welcome_note=models.CharField(max_length=500)
    profile_details=models.TextField()

class faculty_btech(models.Model):
    photo=models.ImageField(upload_to='img',verbose_name='file',null=True,blank=True,default='-')
    name=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)
    dateOf_join=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    designation=models.CharField(max_length=150)
    department=models.CharField(max_length=50)
    experience=models.CharField(max_length=50)
    dateOf_join=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    welcome_note=models.CharField(max_length=500)
    profile_details=models.TextField()

class faculty_mba(models.Model):
    photo=models.ImageField(upload_to='img',verbose_name='file',null=True,blank=True,default='-')
    name=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)
    dateOf_join=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    designation=models.CharField(max_length=150)
    department=models.CharField(max_length=50)
    experience=models.CharField(max_length=50)
    dateOf_join=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    welcome_note=models.CharField(max_length=500)
    profile_details=models.TextField()
class faculty_mca(models.Model):
    photo=models.ImageField(upload_to='img',verbose_name='file',null=True,blank=True,default='-')
    name=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)
    dateOf_join=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    designation=models.CharField(max_length=150)
    department=models.CharField(max_length=50)
    experience=models.CharField(max_length=50)
    dateOf_join=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    welcome_note=models.CharField(max_length=500)
    profile_details=models.TextField()
class faculty_basicscience(models.Model):
    photo=models.ImageField(upload_to='img',verbose_name='file',null=True,blank=True,default='-')
    name=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)
    dateOf_join=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    designation=models.CharField(max_length=150)
    department=models.CharField(max_length=50)
    experience=models.CharField(max_length=50)
    dateOf_join=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    welcome_note=models.CharField(max_length=500)
    profile_details=models.TextField()
class news_updates(models.Model):
    photo=models.ImageField(upload_to='img',verbose_name='file',null=True,blank=True,default='-')
    post_date=models.CharField(max_length=50)
    title=models.CharField(max_length=150)
    details=models.TextField()


class photo_gallery(models.Model):
    gallery_name=models.CharField(max_length=100)
    photo1=models.ImageField(upload_to='img',verbose_name='file',null=True,blank=True,default='-')
    photo2=models.ImageField(upload_to='img',verbose_name='file',null=True,blank=True,default='-')
    photo3=models.ImageField(upload_to='img',verbose_name='file',null=True,blank=True,default='-')
    photo4=models.ImageField(upload_to='img',verbose_name='file',null=True,blank=True,default='-')
    photo5=models.ImageField(upload_to='img',verbose_name='file',null=True,blank=True,default='-')
    photo6=models.ImageField(upload_to='img',verbose_name='file',null=True,blank=True,default='-')
    photo7=models.ImageField(upload_to='img',verbose_name='file',null=True,blank=True,default='-')
    photo8=models.ImageField(upload_to='img',verbose_name='file',null=True,blank=True,default='-')

class media_updates(models.Model):
    title=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='img',verbose_name='file',null=True,blank=True,default='-')
class university_updates(models.Model):
    title=models.CharField(max_length=250)
    pdf = models.FileField()
class university_guidline(models.Model):
    title=models.CharField(max_length=250)
    pdf = models.FileField()

class mandatory_disclosure(models.Model):
    pdf = models.FileField()
    title=models.CharField(max_length=150)
class latest_event(models.Model):
    title1=models.CharField(max_length=200)
    title2=models.CharField(max_length=200)
    post_date=models.CharField(max_length=50)
    details=models.TextField()
class informn_corner(models.Model):
    title=models.CharField(max_length=150)
    pdf = models.FileField()
    photo=models.ImageField(upload_to='img',verbose_name='file',null=True,blank=True,default='-')
    description=models.CharField(max_length=500)
    post_date=models.CharField(max_length=50)
class AICTE_latest_EOA(models.Model):
    title=models.CharField(max_length=150)
    pdf = models.FileField()
class AICTE_previous_EOA(models.Model):
    title=models.CharField(max_length=150)
    pdf = models.FileField()
class application_form(models.Model):
    title=models.CharField(max_length=150)
    pdf = models.FileField()
class brochure(models.Model):
    title=models.CharField(max_length=150)
    pdf = models.FileField()



# class Device(models.Model):

#     type = models.CharField(max_length=200, blank=False)
#     price = models.IntegerField()

#     choices = (
#         ('AVAILABLE', 'Item ready to be purchased'),
#         ('SOLD', 'Item already purchased'),
#         ('RESTOCKING', 'Item restocking in few days')
#     )

#     status = models.CharField(max_length=10, choices=choices, default='SOLD')
#     issues = models.CharField(max_length=50, default="No Issues")

#     class Meta:
#         abstract = True

#     def __str__(self):
#         return 'Type: {0} Price: {1}'.format(self.type, self.price)

# class Desktops(Device):
#     pass

# class Laptops(Device):
#     pass

# class Mobiles(Device):
#     pass







