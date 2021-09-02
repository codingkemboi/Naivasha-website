from django.contrib import admin

# Register your models here.
from .models import *

class HotelAdmin(admin.ModelAdmin):
    search_fields = ("name__startswith", )
    list_display = ('name', 'link', 'image')


admin.site.register(Hotel, HotelAdmin)


class FashonAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'image')


admin.site.register(Fashon, FashonAdmin)


class WildLifeAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'image')


admin.site.register(WildLife, WildLifeAdmin)


class MarketAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'image')


admin.site.register(Market, MarketAdmin)


class OfficeAdmin(admin.ModelAdmin):
    search_fields = ("name__startswith", )
    list_display = ('name', 'link', 'image')


admin.site.register(Office, OfficeAdmin)


class SportAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'image')


admin.site.register(Sport, SportAdmin)


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'image')


admin.site.register(School, SportAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'image')


admin.site.register(News, NewsAdmin)


class FarmAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'image')


admin.site.register(Farm, FarmAdmin)

class TravelAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'image')


admin.site.register(Travel, TravelAdmin)

class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'image')


admin.site.register(Hospital, HospitalAdmin)