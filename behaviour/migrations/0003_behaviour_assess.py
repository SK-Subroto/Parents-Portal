# Generated by Django 2.2.3 on 2019-10-22 22:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('student', '0001_initial'),
        ('behaviour', '0002_behavior_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Behaviour_assess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_post', models.DateTimeField(default=django.utils.timezone.now)),
                ('classAttention', models.IntegerField()),
                ('behaveTeacher', models.IntegerField()),
                ('behaveStudent', models.IntegerField()),
                ('attenClass', models.IntegerField()),
                ('performance', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.Student')),
            ],
        ),
    ]