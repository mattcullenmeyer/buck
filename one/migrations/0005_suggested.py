# Generated by Django 3.1.7 on 2022-01-06 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0004_auto_20220105_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggested',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='one.school')),
                ('suggest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suggest', to='one.school')),
            ],
        ),
    ]
