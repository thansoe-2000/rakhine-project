# Generated by Django 4.2.5 on 2023-09-12 08:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_alter_village_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='ward-image')),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('created', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('township', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.township')),
            ],
        ),
    ]
