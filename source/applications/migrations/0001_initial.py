# Generated by Django 4.1.3 on 2023-01-03 04:18

import applications.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_name', models.CharField(max_length=30, verbose_name='Имя ученика')),
                ('applicant_surname', models.CharField(max_length=30, verbose_name='Фамилия ученика')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Электронная почта ученика')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('school', models.IntegerField(blank=True, help_text='Вводить только цифры', null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Номер школы')),
                ('class_number', models.CharField(blank=True, max_length=3, null=True, verbose_name='Номер класса')),
                ('shift', models.IntegerField(blank=True, help_text='Вводить только цифры', null=True, verbose_name='Номер смены')),
                ('birth_date', models.DateField(blank=True, help_text='Заполнить в формате дд.мм.гггг', max_length=10, null=True, verbose_name='Дата рождения ученика')),
                ('sex', models.CharField(choices=[('MALE', 'Er bala'), ('FEMALE', 'Qyz bala')], default='Undefined', max_length=100, verbose_name='Пол ученика')),
                ('parents_surname', models.CharField(blank=True, max_length=30, null=True, verbose_name='Фамилия родителя')),
                ('parents_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Имя родителя')),
                ('parents_inn', models.PositiveBigIntegerField(blank=True, help_text='Вводить только цифры', null=True, validators=[applications.models.validate_length, django.core.validators.MinValueValidator(0)], verbose_name='ИНН родителя')),
                ('parents_phone', models.CharField(blank=True, max_length=18, null=True, verbose_name='Номер телефона родителя')),
                ('parents_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Электронная почта родителя')),
                ('address', models.CharField(blank=True, help_text='Вводить через запятую: населенный пункт, улица, номер дома, номер квартиры', max_length=200, null=True, verbose_name='Адрес проживания')),
                ('lesson_time', models.CharField(blank=True, max_length=250, null=True, verbose_name='Желательное время обучения')),
                ('sum', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Cумма пакета')),
                ('contract', models.FileField(blank=True, help_text='Загружать pdf подписанного договора', null=True, upload_to='contracts/', verbose_name='Подписанный договор')),
                ('payed', models.BooleanField(default=False, verbose_name='Оплачено')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('discount', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='applications', to='education.discount', verbose_name='Льгота')),
                ('parent', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='application_parent', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Название')),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Доступный статус заявки',
                'verbose_name_plural': 'Доступные статусы заявок',
            },
        ),
        migrations.CreateModel(
            name='ApplicationStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('note', models.TextField(blank=True, max_length=150, verbose_name='Примечание')),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='application_statuses', to='applications.application')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applications.status')),
            ],
            options={
                'verbose_name': 'Установленный статус заявки',
                'verbose_name_plural': 'Установленные статусы заявок',
                'get_latest_by': 'created_at',
            },
        ),
        migrations.AddField(
            model_name='application',
            name='statuses',
            field=models.ManyToManyField(related_name='applications', through='applications.ApplicationStatus', to='applications.status', verbose_name='Статус заявки'),
        ),
        migrations.AddField(
            model_name='application',
            name='student',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='application_student', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='application',
            name='subjects',
            field=models.ManyToManyField(blank=True, related_name='applications', to='education.subject'),
        ),
    ]
