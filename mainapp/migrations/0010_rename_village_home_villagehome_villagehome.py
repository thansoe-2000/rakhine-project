# Generated by Django 4.2.5 on 2023-09-16 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_villagehome_townshipward'),
    ]

    operations = [
        migrations.RenameField(
            model_name='villagehome',
            old_name='village_home',
            new_name='villagehome',
        ),
    ]