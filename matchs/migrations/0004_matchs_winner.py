# Generated by Django 4.0.1 on 2022-05-04 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matchs', '0003_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchs',
            name='winner',
            field=models.IntegerField(default=0),
        ),
    ]
