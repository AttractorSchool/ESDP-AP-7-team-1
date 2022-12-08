from django.contrib import admin
from education.models import Subject
from education.models import ApplicationStatus, Status, Application

'''Декоратор регистрирует в админ панели модель'''
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    '''Лист дисплэй выводит все поля из модели'''
    list_display = [field.name for field in Subject._meta.fields]
    
@admin.register(ApplicationStatus)
class ApplicationStatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ApplicationStatus._meta.fields]
    
@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]
    
@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Application._meta.fields]
