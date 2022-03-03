# Generated by Django 3.2.4 on 2021-08-17 09:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0020_tournament_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='user',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Tournament', to=settings.AUTH_USER_MODEL),
        ),
    ]
