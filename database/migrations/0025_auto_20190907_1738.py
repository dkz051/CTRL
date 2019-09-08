# Generated by Django 2.2.5 on 2019-09-07 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0024_auto_20190907_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='hit',
        ),
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Team'),
        ),
        migrations.AlterField(
            model_name='relation',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Team'),
        ),
    ]