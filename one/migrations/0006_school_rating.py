# Generated by Django 3.1.7 on 2022-01-06 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0005_auto_20220106_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]