# Generated by Django 2.2.1 on 2019-07-27 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classdairy', '0007_classdairy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classdairy',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classdairies', to=settings.AUTH_USER_MODEL),
        ),
    ]
