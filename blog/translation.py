from modeltranslation.translator import TranslationOptions, register
from django.contrib import admin
from .models import Contact, Steps, Card, Team, CallBack


@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ('address', 'start_work', 'finish_work', 'work_created_at', 'work_updated_at', 'phone_number', 
        'facebook_link', 'linkedin_link', 'youtube_link', 'instagram_link')
    


@register(Steps)
class StepsTranslationOptions(TranslationOptions):
    fields = ('title', 'body')


@register(Card)
class CardTranslationOptions(TranslationOptions):
    fields = ('title', 'body')


@register(Team)
class CardTranslationOptions(TranslationOptions):
    fields = ('title', 'work', 'position')


