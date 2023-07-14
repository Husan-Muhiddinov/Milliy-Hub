from django.shortcuts import render
from django.views import View
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Contact, Steps, Card, Team, CallBack, Blog, Comment, Services, OurTeam, About, Faqs, Our_keys_of_service, \
        Testimonial, Addvertising, Finansial, Trade_Stock, Audit_Assuranse, Saving, Strategic, DepartmentContact, Keys_of_service, Footer_Email
# Create your views here.

def for_all_pages(request):
    blog = Blog.objects.all()
    b=Blog.objects.all().order_by('-id')[:2]
    contac= Contact.objects.all().last()
    if request.method == 'POST':
        call = Footer_Email(
            email=request.POST['email'],
        )
        call.save()
        messages.success(request, "Succesfully Created")
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
    fina = Keys_of_service.objects.all().first()
    text = Finansial.objects.all().last()
    context = {
        'finan': finan,
        'fina': fina,
        'text': text,
    }
    return render(request, 'financial-planning.html', context=context)


def trade_stock(request):
    finan = Our_keys_of_service.objects.all()
    fina = Keys_of_service.objects.all().first()
    text = Trade_Stock.objects.all().last()
    context = {
        'finan': finan,
        'fina': fina,
        'text': text,
    }
    return render(request, 'trade-and-stock.html', context=context)


def audit_assurance(request):
    finan = Our_keys_of_service.objects.all()
    fina = Keys_of_service.objects.all().first()
    text = Audit_Assuranse.objects.all().last()
    context = {
        'finan': finan,
        'fina': fina,
        'text': text,
    }
    return render(request, 'audit-and-assurance.html', context=context)


def saving_strategy(request):
    finan = Our_keys_of_service.objects.all()
    fina = Keys_of_service.objects.all().first()
    text = Saving.objects.all().last()
    context = {
        'finan': finan,
        'fina': fina,
        'text': text,
    }
    return render(request, 'saving-strategy.html', context=context)


def strategic_planning(request):
    finan = Our_keys_of_service.objects.all()
    fina = Keys_of_service.objects.all().first()
    text = Strategic.objects.all().last()
    context = {
        'finan': finan,
        'fina': fina,
        'text': text,
    }
    return render(request, 'Strategic-planning.html', context=context)


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

    paginator = Paginator(blog, 2)

    page = request.GET.get('page', 1)

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
    if request.method == 'POST':
        contact = DepartmentContact(
            name=request.POST['username'],
            email=request.POST['email'],
            message=request.POST['message'],
        )
        contact.save()
        list(messages.get_messages(request))
        messages.success(request, "Succesfully Created", fail_silently=True)
    context = {
        'contac': contac, 
        }
    return render(request, 'contact.html', context=context)