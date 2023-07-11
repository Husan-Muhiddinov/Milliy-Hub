from django.shortcuts import render
from django.views import View
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Contact, Steps, Card, Team, CallBack, Blog, Comment, Services, OurTeam, About, Faqs, Our_keys_of_service, Testimonial, Addvertising, Finansial, Trade_Stock, Audit_Assuranse, Saving, Strategic
# Create your views here.

def for_all_pages(request):
    blog = Blog.objects.all()
    b=Blog.objects.all().order_by('-id')[:2]
    contac= Contact.objects.all().last()
    return {'contac': contac, 'b': b, 'blog': blog}


def index(request):
    contac= Contact.objects.all().last()
    step = Steps.objects.all()
    card = Card.objects.all()
    blog = Blog.objects.all()
    t = Team.objects.all().order_by('-id')[:3]
    advert = Addvertising.objects.all()
    test = Testimonial.objects.all()
    a=Blog.objects.all().order_by('-id')[:2]
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
        'blog': blog,
        'a': a,
        'test': test,
        'advert': advert,
        't': t,
        }
    return render(request, "index-3.html", context=context)


def about(request):
    abot = About.objects.all().last()
    step = Steps.objects.all()
    faq = Faqs.objects.all()
    test = Testimonial.objects.all()
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
        'abot': abot,
        'faq': faq,
        'test': test,
        }
    return render(request, 'about.html', context=context)


def services(request):
    servic = Services.objects.all()
    advert = Addvertising.objects.all()
    card = Card.objects.all()
    context = {
        'servic': servic,
        'card': card,
        'advert': advert,
    }
    return render(request, 'services.html', context=context)


def financial(request):
    finan = Our_keys_of_service.objects.all()
    fina = Our_keys_of_service.objects.all().last()
    context = {
        'finan': finan,
        'fina': fina,
    }
    return render(request, 'financial-planning.html', context=context)


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
    team = Team.objects.all()
    advert = Addvertising.objects.all()
    context = {
        'advert': advert,
        'team': team,
    }
    return render(request, 'cases.html', context=context)


def case_detail(request, case_id):
    team = Team.objects.get(pk=case_id)
    context = {
        'team': team,
    }
    return render(request, 'case-detail.html', context=context)


def pricing(request):
    return render(request, 'pricing.html')


def team(request):
    ourteam = OurTeam.objects.all()
    context = {
        'ourteam': ourteam,
    }
    return render(request, 'team.html', context=context)


def blog(request):
    blog = Blog.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(blog, 2)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'blog': blog, 
        'posts': posts,
        }
    return render(request, 'blog.html', context=context)


def blog_detail(request, blog_id):
    blog = Blog.objects.get(pk=blog_id)
    c=Blog.objects.all().order_by('-id')[:3]
    contac= Contact.objects.all().last()
    context = {
        'blog': blog,
        'c': c,
        'contac': contac,
    }
    return render(request, 'blog-detail.html', context=context)


def contact(request):
    contac= Contact.objects.all().last()
    context = {
        'contac': contac, 
        }
    return render(request, 'contact.html', context=context)