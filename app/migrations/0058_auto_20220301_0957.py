# Generated by Django 3.0.7 on 2022-03-01 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0057_auto_20220301_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admins',
            name='name',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='admins',
            name='title',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]
