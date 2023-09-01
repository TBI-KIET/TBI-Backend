from django.contrib import admin

from .models import Events
from django.contrib import admin

class EventsAdmin(admin.ModelAdmin):
    list_display = ('title','occured')
    list_filter = ('occured',)

admin.site.register(Events)