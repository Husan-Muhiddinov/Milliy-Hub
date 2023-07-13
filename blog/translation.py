from modeltranslation.translator import TranslationOptions, register
from django.contrib import admin
from .models import Contact, Steps, Card, Team, CallBack, Blog, Services, OurTeam, About, Faqs, Our_keys_of_service, Testimonial, Finansial, Trade_Stock, Audit_Assuranse, Saving, Strategic


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
class TeamTranslationOptions(TranslationOptions):
    fields = ('title', 'work', 'position', 'detail_title', 'summary', 'body', 'client_name', 'location', 'project_under', 'advisor')


@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'summary', 'body', 'day')


@register(Services)
class ServicesTranslationOptions(TranslationOptions):
    fields = ('title', 'summary', 'body')


@register(OurTeam)
class OurTeamTranslationOptions(TranslationOptions):
    fields = ('name', 'job')


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'body', 'our_mission', 'our_vision')


@register(Faqs)
class FaqsTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')


@register(Our_keys_of_service)
class Our_keys_of_serviceTranslationOptions(TranslationOptions):
    fields = ('title', 'body', 'benifits', 'mutual_funds', 'company_growth')



@register(Testimonial)
class TestimonialTranslationOptions(TranslationOptions):
    fields = ('name', 'position', 'description')



@register(Finansial)
class FinansialTranslationOptions(TranslationOptions):
    fields = ('body',)



@register(Trade_Stock)
class Trade_StockTranslationOptions(TranslationOptions):
    fields = ('body',)


@register(Audit_Assuranse)
class Audit_AssuranseTranslationOptions(TranslationOptions):
    fields = ('body',)


@register(Saving)
class SavingTranslationOptions(TranslationOptions):
    fields = ('body',)


@register(Strategic)
class StrategicTranslationOptions(TranslationOptions):
    fields = ('body',)

