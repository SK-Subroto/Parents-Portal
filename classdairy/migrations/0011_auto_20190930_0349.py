# Generated by Django 2.2.3 on 2019-09-30 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classdairy', '0010_auto_20190930_0348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classdairy',
            name='subject',
            field=models.CharField(choices=[('Bangla', 'Bangla'), ('English', 'English')], default='English', max_length=50),
        ),
    ]
