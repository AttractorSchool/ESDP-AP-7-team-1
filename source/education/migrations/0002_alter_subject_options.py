# Generated by Django 4.1.3 on 2022-12-08 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subject',
            options={'verbose_name': 'Предмет', 'verbose_name_plural': 'Предметы'},
        ),
    ]
