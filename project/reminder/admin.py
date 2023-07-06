from django.contrib import admin

from .models import ReminderModel


# class ReminderAdmin(admin.ModelAdmin):
#     prepopulated_fields = ...

admin.site.register(ReminderModel)
