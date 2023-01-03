from django.contrib import admin

from applications.models import (Application, ApplicationStatus, Status)


@admin.register(ApplicationStatus)
class ApplicationStatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ApplicationStatus._meta.fields]


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Application._meta.fields]
