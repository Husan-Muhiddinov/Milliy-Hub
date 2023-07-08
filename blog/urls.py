from django.urls import path
from .views import index, about, services, financial, trade_stock, audit_assurance, saving_strategy, strategic_planning, service_detail,\
    cases, case_detail, pricing, team, blog, blog_detail, contact

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('financial/', financial, name='financial'),
    path('trade_stock/', trade_stock, name='trade_stock'),
    path('audit_assurance/', audit_assurance, name='audit_assurance'),
    path('saving_strategy/', saving_strategy, name='saving_strategy'),
    path('strategic_planning/', strategic_planning, name='strategic_planning'),
    path('<int:servic_id>/service_detail/', service_detail, name='service_detail'),
    path('cases/', cases, name='cases'),
    path('case_detail/', case_detail, name='case_detail'),
    path('pricing/', pricing, name='pricing'),
    path('team/', team, name='team'),
    path('blog/', blog, name='blog'),
    path('<int:blog_id>/blog_detail/', blog_detail, name='blog_detail'),
    path('contact/', contact, name='contact'),
]