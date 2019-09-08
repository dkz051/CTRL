# Generated by Django 2.2.5 on 2019-09-07 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0026_auto_20190907_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='first_name',
            field=models.CharField(max_length=255, verbose_name='名'),
        ),
        migrations.AlterField(
            model_name='player',
            name='full_name',
            field=models.CharField(max_length=255, verbose_name='全名'),
        ),
        migrations.AlterField(
            model_name='player',
            name='last_name',
            field=models.CharField(max_length=255, verbose_name='姓'),
        ),
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Team', verbose_name='所属球队'),
        ),
        migrations.AlterField(
            model_name='relation',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.Team'),
        ),
    ]