# Generated by Django 3.2.8 on 2021-10-21 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20211017_1937'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='data',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='article',
            name='slug',
        ),
    ]
