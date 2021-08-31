from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.
from .models import *


def home(request):
    return render(request, 'naivasha/home.html')


def about(request):
    return render(request, 'naivasha/about.html')

# @login_required
def hotel(request):
    try: 
        hotels = Hotel.objects.all()
    except Hotel.DoesNotExist:
        raise Http404
    context = {'hotel': hotels}
    return render(request, 'naivasha/hotels.html', context)

# @login_required
def fashon(request):
    fashons = Fashon.objects.all()
    context = {'fashon': fashons}
    return render(request, 'naivasha/fashons.html', context)

# @login_required
def market(request):
    markets = Market.objects.all()
    context = {'market': markets}
    return render(request, 'naivasha/markets.html', context)

# @login_required
def news(request):
    news = News.objects.all()
    context = {'news': news}
    return render(request, 'naivasha/news.html', context)

# @login_required
def wild_life(request):
    animals = WildLife.objects.all()
    context = {'animal': animals}
    return render(request, 'naivasha/wildLife.html', context)

# @login_required
def farm(request):
    farms = Farm.objects.all()
    context = {'farm': farms}
    return render(request, 'naivasha/farming.html', context)

# @login_required
def office(request):
    offices = Office.objects.all()
    context = {'offices': offices}
    return render(request, 'naivasha/offices.html', context)

# @login_required
def school(request):
    schools = School.objects.all()
    context = {'school': schools}
    return render(request, 'naivasha/schools.html', context)

# @login_required
def sport(request):
    sports = Sport.objects.all()
    context = {'sport': sports}
    return render(request, 'naivasha/sports.html', context)
    
# @login_required
def hospital(request):
    hospitals = Hospital.objects.all()
    context = {'hospital': hospitals}
    return render(request, 'naivasha/hospitals.html', context)

# @login_required
def travel(request):
    travels = Travel.objects.all()
    context = {'travels': travels}
    return render(request, 'naivasha/travels.html', context)


def contact(request):
    return render(request, 'naivasha/contacts.html')


def error_404(request, exception):
    return render(request, '404.html')


def error_403(request, exception):
    return render(request, '403.html')


def error_400(request, exception):
    return render(request, '400.html')


def error_500(request, exception):
    return render(request, '500.html')    