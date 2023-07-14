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
    list_display = ['image','title', 'work', 'position', 'detail_title', 'summary', 'body', 'client_name', 'location', 'project_value', 'year_completed', 'project_under', 'advisor']


@admin.register(CallBack)
class CallBackModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'message']


@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['blog', 'comment']


@admin.register(Blog)
class BlogModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'summary', 'body', 'author', 'photo']


@admin.register(Services)
class ServicesModelAdmin(MyTranslationAdmin):
    list_display = ['icon','title', 'summary', 'body', 'photo']


@admin.register(OurTeam)
class OurTeamModelAdmin(MyTranslationAdmin):
    list_display = ['image','name', 'job', 'facebook_link', 'instagram_link', 'email']


@admin.register(About)
class AboutModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'body', 'consultants', 'awards', 'cases', 'our_mission', 'our_vision']


@admin.register(Faqs)
class FaqsModelAdmin(MyTranslationAdmin):
    list_display = ['question', 'answer']


@admin.register(Our_keys_of_service)
class Our_keys_of_serviceModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'body']


@admin.register(Keys_of_service)
class Keys_of_serviceModelAdmin(MyTranslationAdmin):
    list_display = ['benifits', 'mutual_funds', 'company_growth']

    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)



@admin.register(Testimonial)
class TestimonialModelAdmin(MyTranslationAdmin):
    list_display = ['image', 'name', 'position', 'description']



@admin.register(Addvertising)
class AddvertisingModelAdmin(admin.ModelAdmin):
    list_display = ['photo', 'link']


@admin.register(Footer_Email)
class Footer_EmailModelAdmin(admin.ModelAdmin):
    list_display = ['email']



@admin.register(Finansial)
class FinansialModelAdmin(MyTranslationAdmin):
    list_display = ['body']

    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)


@admin.register(Trade_Stock)
class Trade_StockModelAdmin(MyTranslationAdmin):
    list_display = ['body']

    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)



@admin.register(Audit_Assuranse)
class Audit_AssuranseModelAdmin(MyTranslationAdmin):
    list_display = ['body']

    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)



@admin.register(Saving)
class SavingModelAdmin(MyTranslationAdmin):
    list_display = ['body']

    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)




@admin.register(Strategic)
class StrategicModelAdmin(MyTranslationAdmin):
    list_display = ['body']

    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)
    

@admin.register(DepartmentContact)
class DepartmentContactModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']