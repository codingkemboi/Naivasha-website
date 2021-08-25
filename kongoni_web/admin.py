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


class StationAdmin(admin.ModelAdmin):
    search_fields = ("name__startswith", )
    list_display = ('name', 'link', 'image')


admin.site.register(Station, StationAdmin)


class SportAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'image')


admin.site.register(Sport, SportAdmin)


class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'image')


admin.site.register(School, SportAdmin)


class TrendAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'image')


admin.site.register(Trend, TrendAdmin)


class LakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'image')


admin.site.register(Lake, LakeAdmin)

class TourismAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'image')


admin.site.register(Tourism, TourismAdmin)
