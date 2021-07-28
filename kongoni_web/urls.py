
from django.urls import path
from kongoni_web import views
from django.views.static import serve
from django.conf.urls import handler404



app_name = 'kongoni_web'
urlpatterns = [
    path('', views.home, name='home'),
    path('hotels/', views.hotel, name='hotels'),
    path('wildlife/', views.wild_life, name='wildlife'),
    path('markets/', views.market, name='markets'),
    path('sports/', views.sport, name='sports'),
    path('trends/', views.trend, name='trends'),
    path('schools/', views.school, name='schools'),
    path('about/', views.about, name='about'),
    path('lakes/', views.lake, name='lakes'),
    path('police/', views.station, name='station'),
    path('fashons/', views.fashon, name='fashons'),
    path('hospitals/', views.hospital, name='hospitals'),
    path('contacts/', views.contact, name='contacts'),
]


handler404 = "kongoni_web.views.error_404"
handler404 = "kongoni_web.views.error_500"
handler404 = "kongoni_web.views.error_403"
handler404 = "kongoni_web.views.error_400"