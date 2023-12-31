# Generated by Django 4.2.4 on 2023-09-10 03:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_township'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='created',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='district',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='township',
            name='created',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='township',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
