from django.contrib import admin
from education.models import Subject
from education.models import ApplicationStatus, Status, Application
from education.models import Class, StudentGroup, Schedule

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


@admin.register(Class)
class GroupAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Class._meta.fields]


@admin.register(StudentGroup)
class StudentGroupAdmin(admin.ModelAdmin):
    list_display = [field.name for field in StudentGroup._meta.fields]


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Schedule._meta.fields]
