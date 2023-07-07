from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.




class Contact(models.Model):
    email = models.EmailField(null=True, verbose_name=_('email'))
    address = models.CharField(max_length=50, null=True, verbose_name=_('address'))
    start_work = models.CharField(max_length=10, null=True, verbose_name=_('start_work'))
    finish_work = models.CharField(max_length=10, null=True, verbose_name=_('finish_work'))
    work_created_at = models.TimeField(null=True, verbose_name=_('work_created_at'))
    work_updated_at = models.TimeField(null=True, verbose_name=_('work_updated_at'))
    phone_number = models.CharField(max_length=17, null=True, verbose_name=_('phone_number'))
    facebook_link = models.CharField(max_length=30, null=True, verbose_name=_('facebook_link'))
    linkedin_link = models.CharField(max_length=30, null=True, verbose_name=_('linkedin_link'))
    youtube_link = models.CharField(max_length=30, null=True, verbose_name=_('youtube_link'))
    instagram_link = models.CharField(max_length=30, null=True, verbose_name=_('instagram_link'))

    def __str__(self):
        return self.email
    

class Steps(models.Model):
    title = models.CharField(max_length=30, null=True, verbose_name=_('title'))
    body = models.CharField(max_length=100, null=True, verbose_name=_('body'))

    def __str__(self):
        return self.title
    

class Card(models.Model):
    icon = models.CharField(max_length=50, null=True, verbose_name=_('icon'))
    title = models.CharField(max_length=50, null=True, verbose_name=_('title'))
    body = models.CharField(max_length=50, null=True, verbose_name=_('body'))

    def __str__(self):
        return self.title
    

class Team(models.Model):
    image = models.ImageField(upload_to="team_images", null=True, verbose_name=_('image'))
    title = models.CharField(max_length=30, null=True, verbose_name=_('title'))
    work = models.CharField(max_length=30, null=True, verbose_name=_('work'))
    position = models.CharField(max_length=30, null=True, verbose_name=_('position'))

    def __str__(self):
        return self.title
    

class CallBack(models.Model):
    name = models.CharField(max_length=30, null=True, verbose_name=_('name'))
    email = models.EmailField(null=True, verbose_name=_('email'))
    subject = models.CharField(max_length=30, null=True, verbose_name=_('subject'))
    message = models.CharField(max_length=70, null=True, verbose_name=_('messages'))

    def __str__(self):
        return self.name