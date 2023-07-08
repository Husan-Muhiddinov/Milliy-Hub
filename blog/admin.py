from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
# Register your models here.



class MyTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(Contact)
class ContactModelAdmin(MyTranslationAdmin):
    list_display = ['email', 'address', 'start_work', 'finish_work', 'work_created_at', 'work_updated_at', 'phone_number', 
        'facebook_link', 'linkedin_link', 'youtube_link', 'instagram_link']
    

@admin.register(Steps)
class StepsModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'body']


@admin.register(Card)
class CardModelAdmin(admin.ModelAdmin):
    list_display = ['icon','title', 'body']


@admin.register(Team)
class TeamModelAdmin(MyTranslationAdmin):
    list_display = ['image','title', 'work', 'position']


@admin.register(CallBack)
class CallBackModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message']


@admin.register(Comment)
class CommentkModelAdmin(admin.ModelAdmin):
    list_display = ['blog', 'comment']


@admin.register(Blog)
class BlogModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'summary', 'body', 'author', 'photo', 'day']


@admin.register(Services)
class ServicesModelAdmin(MyTranslationAdmin):
    list_display = ['icon','title', 'summary', 'body', 'photo']