# Generated by Django 4.2.5 on 2023-09-10 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_village'),
    ]

    operations = [
        migrations.AlterField(
            model_name='village',
            name='image',
            field=models.ImageField(upload_to='village-image'),
        ),
    ]
