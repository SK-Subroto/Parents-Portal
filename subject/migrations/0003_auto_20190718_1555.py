# Generated by Django 2.2.1 on 2019-07-18 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0002_auto_20190718_1547'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='sub',
            new_name='clss',
        ),
        migrations.AddField(
            model_name='subject',
            name='sub_name',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
