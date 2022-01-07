# Generated by Django 3.1.7 on 2022-01-06 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0003_suggested'),
    ]

    operations = [
        migrations.AddField(
            model_name='suggested',
            name='address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='suggested',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='suggested',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='suggested',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, null=True),
        ),
    ]