from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.
from .models import *


def home(request):
    return render(request, 'kongoni/home.html')


def about(request):
    return render(request, 'kongoni/about.html')

@login_required
def hotel(request):
    try: 
        hotels = Hotel.objects.all()
    except Hotel.DoesNotExist:
        raise Http404
    context = {'hotel': hotels}
    return render(request, 'kongoni/hotels.html', context)

@login_required
def fashon(request):
    fashons = Fashon.objects.all()
    context = {'fashon': fashons}
    return render(request, 'kongoni/fashons.html', context)

@login_required
def market(request):
    markets = Market.objects.all()
    context = {'market': markets}
    return render(request, 'kongoni/markets.html', context)

@login_required
def trend(request):
    trends = Trend.objects.all()
    context = {'trend': trends}
    return render(request, 'kongoni/trends.html', context)

@login_required
def wild_life(request):
    animals = WildLife.objects.all()
    context = {'animal': animals}
    return render(request, 'kongoni/wildLife.html', context)

@login_required
def lake(request):
    lakes = Lake.objects.all()
    context = {'lake': lakes}
    return render(request, 'kongoni/lakes.html', context)

@login_required
def station(request):
    polices = Station.objects.all()
    context = {'police': polices}
    return render(request, 'kongoni/station.html', context)

@login_required
def school(request):
    schools = School.objects.all()
    context = {'school': schools}
    return render(request, 'kongoni/schools.html', context)

@login_required
def sport(request):
    sports = Sport.objects.all()
    context = {'sport': sports}
    return render(request, 'kongoni/sports.html', context)
    
@login_required
def hospital(request):
    hospitals = Hospital.objects.all()
    context = {'hospital': hospitals}
    return render(request, 'kongoni/hospitals.html', context)


def contact(request):
    return render(request, 'kongoni/contacts.html')


def error_404(request, exception):
    return render(request, '404.html')


def error_403(request, exception):
    return render(request, '403.html')


def error_400(request, exception):
    return render(request, '400.html')


def error_500(request, exception):
    return render(request, '500.html')    