from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
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
    body = models.TextField(max_length=100, null=True, verbose_name=_('body'))

    def __str__(self):
        return self.title
    

class Card(models.Model):
    icon = models.CharField(max_length=50, null=True, verbose_name=_('icon'))
    title = models.CharField(max_length=50, null=True, verbose_name=_('title'))
    body = models.TextField(max_length=50, null=True, verbose_name=_('body'))

    def __str__(self):
        return self.title
    

class Team(models.Model):
    image = models.ImageField(upload_to="team_images", null=True, verbose_name=_('image'))
    title = models.CharField(max_length=100, null=True, verbose_name=_('title'))
    work = models.CharField(max_length=70, null=True, verbose_name=_('work'))
    position = models.CharField(max_length=50, null=True, verbose_name=_('position'))

    def __str__(self):
        return self.title
    

class CallBack(models.Model):
    name = models.CharField(max_length=50, null=True, verbose_name=_('name'))
    email = models.EmailField(null=True, verbose_name=_('email'))
    subject = models.CharField(max_length=100, null=True, verbose_name=_('subject'))
    message = models.CharField(max_length=70, null=True, verbose_name=_('messages'))

    def __str__(self):
        return self.name
    


class Blog(models.Model):
    title=models.CharField(max_length=250, null=True, verbose_name=_('title'))
    summary=models.CharField(max_length=500, null=True, verbose_name=_('summary'))
    body=RichTextField(verbose_name=_('body'))
    # body=models.CharField(max_length=900, null=True, verbose_name=_('body'))
    author = models.CharField(max_length=70, null=True, verbose_name=_('author'))
    photo=models.ImageField(upload_to='images',blank=True, null=True, verbose_name=_('photo'))
    day=models.DateTimeField(auto_now_add=True, null=True, verbose_name=_('day'))
    updated_at=models.DateTimeField(auto_now_add=True, null=True, verbose_name=_('updated_at'))

    class Meta:
        ordering = ["-id"]



    def __str__(self):
        return self.title
    

class Comment(models.Model):
    blog=models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name=_('blog'))
    comment=models.CharField(max_length=150, verbose_name=_('comment'))
    # author=models.ForeignKey(
    #     get_user_model(),
    #     on_delete=models.CASCADE,
    # )

    def __str__(self):
        return self.comment
    

class Services(models.Model):
    icon = models.CharField(max_length=50, null=True, verbose_name=_('icon'))
    title=models.CharField(max_length=250, null=True, verbose_name=_('title'))
    summary=models.TextField(null=True, verbose_name=_('summary'))
    body=models.TextField(null=True, verbose_name=_('body'))
    photo=models.ImageField(upload_to='images', null=True, verbose_name=_('photo'))

    def __str__(self):
        return self.title
    

class OurTeam(models.Model):
    image = models.ImageField(upload_to="team_images", null=True, verbose_name=_('image'))
    name = models.CharField(max_length=50, null=True, verbose_name=_('name'))
    job = models.CharField(max_length=50, null=True, verbose_name=_('job'))
    facebook_link = models.CharField(max_length=30, null=True, verbose_name=_('facebook_link'))
    instagram_link = models.CharField(max_length=30, null=True, verbose_name=_('instagram_link'))
    email = models.EmailField(null=True, verbose_name=_('email'))

    def __str__(self):
        return self.name



class About(models.Model):
    title = models.CharField(max_length=250, null=True, verbose_name=_('title'))
    body=models.TextField(null=True, verbose_name=_('body'))
    consultants = models.IntegerField(null=True, verbose_name=_('consultants'))
    awards = models.IntegerField(null=True, verbose_name=_('awards'))
    cases = models.IntegerField(null=True, verbose_name=_('cases'))
    our_mission = models.CharField(max_length=255, null=True, verbose_name=_('our_mission'))
    our_vision = models.CharField(max_length=255, null=True, verbose_name=_('our_vision'))


    def __str__(self):
        return self.title
    

class Faqs(models.Model):
    question = models.TextField(null=True, verbose_name=_('question'))
    answer = models.TextField(null=True, verbose_name=_('answer'))

    def __str__(self):
        return self.question
    

class Our_keys_of_service(models.Model):
    title = models.CharField(max_length=250, null=True, verbose_name=_('title'))
    body=models.TextField(null=True, verbose_name=_('body'))
    benifits=models.TextField(null=True, verbose_name=_('benifits'))
    mutual_funds=models.TextField(null=True, verbose_name=_('mutual_funds'))
    company_growth=models.TextField(null=True, verbose_name=_('company_growth'))

    def __str__(self):
        return self.title
    

class Testimonial(models.Model):
    image = models.ImageField(upload_to="team_images", null=True, verbose_name=_('image'))
    name = models.CharField(max_length=30, null=True, verbose_name=_('name'))
    position = models.CharField(max_length=50, null=True, verbose_name=_('position'))
    description = models.TextField(null=True, verbose_name=_('description'))

    def __str__(self):
        return self.name
    

class Addvertising(models.Model):
    photo=models.ImageField(upload_to='images', null=True, verbose_name=_('photo'))
    link = models.CharField(max_length=100, null=True, verbose_name=_('link'))

    def __str__(self):
        return self.link