# Generated by Django 4.0.1 on 2022-03-29 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0003_remove_player_team_id_player_captain_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='team_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='player.team'),
            preserve_default=False,
        ),
    ]
