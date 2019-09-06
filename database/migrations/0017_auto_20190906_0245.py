# Generated by Django 2.2.5 on 2019-09-06 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0016_auto_20190905_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='news',
            name='source',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='player',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='player',
            name='full_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='player',
            name='last_name',
            field=models.CharField(max_length=255),
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
        migrations.AlterField(
            model_name='team',
            name='area',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='team',
            name='arena',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='team',
            name='full_en_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='team',
            name='full_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='joined',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='team',
            name='short_name',
            field=models.CharField(max_length=255),
        ),
    ]