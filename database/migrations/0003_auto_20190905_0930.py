# Generated by Django 2.2.5 on 2019-09-05 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_team_player'),
    ]

    operations = [
        migrations.DeleteModel(
            name='team_player',
        ),
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.team'),
        ),
    ]
