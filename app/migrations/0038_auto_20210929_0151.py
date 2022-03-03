# Generated by Django 3.2.4 on 2021-09-29 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0037_auto_20210929_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='draws',
            field=models.PositiveIntegerField(blank=True, default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='lose',
            field=models.PositiveIntegerField(blank=True, default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='team',
            name='win',
            field=models.PositiveIntegerField(blank=True, default=0, max_length=100),
        ),
    ]
