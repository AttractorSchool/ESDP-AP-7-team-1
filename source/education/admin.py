from django.contrib import admin

from education.models import (Auditorium, ClassTime, Discount, Grouping,
                              GroupingStatus, Packet, Schedule,
                              StatusOfGrouping, StudentGrouping, Subject,
                              TeacherGrouping)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    """Декоратор регистрирует в админ панели модель
       Лист дисплэй выводит все поля из модели"""
    list_display = [field.name for field in Subject._meta.fields]


@admin.register(Grouping)
class GroupingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Grouping._meta.fields]


@admin.register(StudentGrouping)
class StudentGroupingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in StudentGrouping._meta.fields]


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Schedule._meta.fields]


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Discount._meta.fields]


@admin.register(Packet)
class PacketAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Packet._meta.fields]


@admin.register(GroupingStatus)
class GroupingStatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in GroupingStatus._meta.fields]


@admin.register(StatusOfGrouping)
class StatusOfGroupingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in StatusOfGrouping._meta.fields]


@admin.register(TeacherGrouping)
class TeacherGroupingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in TeacherGrouping._meta.fields]


@admin.register(ClassTime)
class ClassTimeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ClassTime._meta.fields]


@admin.register(Auditorium)
class AuditoriumAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Auditorium._meta.fields]
