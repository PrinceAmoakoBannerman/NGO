from django.contrib import admin
from .models import Volunteer, Donation, Event
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'date_joined', 'mobile_number')
    search_fields = ('user__username', 'user__email', 'mobile_number')
    list_filter = ('status',)

@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('donor', 'amount', 'date', 'message')
    search_fields = ('donor__username', 'donor__email')
    list_filter = ('date',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'location')
    search_fields = ('name', 'location')
    list_filter = ('date',)
    

