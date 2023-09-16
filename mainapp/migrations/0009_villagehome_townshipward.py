# Generated by Django 4.2.5 on 2023-09-16 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_ward'),
    ]

    operations = [
        migrations.CreateModel(
            name='VillageHome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_id', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=100)),
                ('village_home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.village')),
            ],
        ),
        migrations.CreateModel(
            name='TownshipWard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_id', models.CharField(max_length=100)),
                ('owner', models.CharField(max_length=100)),
                ('township_home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.township')),
            ],
        ),
    ]