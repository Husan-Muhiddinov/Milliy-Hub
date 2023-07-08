from django.shortcuts import render
from django.views import View
from django.contrib import messages
from .models import Contact, Steps, Card, Team, CallBack, Blog, Comment, Services
# Create your views here.

def for_all_pages(request):
    contac= Contact.objects.all().last()
    return {"contac": contac}


def index(request):
    contac= Contact.objects.all().last()
    step = Steps.objects.all()
    card = Card.objects.all()
    team = Team.objects.all()
    if request.method == 'POST':
        call = CallBack(
            name=request.POST['username'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        call.save()
        messages.success(request, "Succesfully Created")
    context = {
        'contac': contac, 
        'step': step, 
        'card': card, 
        'team': team, 
        }
    return render(request, "index-3.html", context=context)


def about(request):
    step = Steps.objects.all()
    if request.method == 'POST':
        call = CallBack(
            name=request.POST['username'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        call.save()
        messages.success(request, "Succesfully Created")
    context = {
        'step': step,
        }
    return render(request, 'about.html', context=context)


def services(request):
    servic = Services.objects.all()
    card = Card.objects.all()
    context = {
        'servic': servic,
        'card': card,
    }
    return render(request, 'services.html', context=context)


def financial(request):
    return render(request, 'financial-planning.html')


def trade_stock(request):
    return render(request, 'trade-and-stock.html')


def audit_assurance(request):
    return render(request, 'audit-and-assurance.html')


def saving_strategy(request):
    return render(request, 'saving-strategy.html')


def strategic_planning(request):
    return render(request, 'Strategic-planning.html')


def service_detail(request, servic_id):
    servic = Services.objects.get(pk=servic_id)
    context = {
        'servic': servic,
    }
    return render(request, 'service-detail.html', context=context)


def cases(request):
    return render(request, 'cases.html')


def case_detail(request):
    return render(request, 'case-detail.html')


def pricing(request):
    return render(request, 'pricing.html')


def team(request):
    return render(request, 'team.html')


def blog(request):
    blog = Blog.objects.all()
    context = {
        'blog': blog, 
        }
    return render(request, 'blog.html', context=context)


def blog_detail(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    context = {
        'blog': blog,
    }
    return render(request, 'blog-detail.html', context=context)


def contact(request):
    return render(request, 'contact.html')