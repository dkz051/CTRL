# Generated by Django 2.2.5 on 2019-09-05 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_auto_20190905_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='team',
            field=models.CharField(max_length=512),
        ),
    ]