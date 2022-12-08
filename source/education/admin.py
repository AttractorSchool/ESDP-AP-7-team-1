from django.contrib import admin
from education.models import Subject

'''Декоратор регистрирует в админ панели модель'''
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    '''Лист дисплэй выводит все поля из модели'''
    list_display = [field.name for field in Subject._meta.fields]
    