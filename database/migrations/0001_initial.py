# Generated by Django 2.2.5 on 2019-09-05 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news_entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1024)),
                ('published', models.DateTimeField()),
                ('source', models.CharField(max_length=2048)),
                ('image', models.CharField(max_length=2048)),
                ('content', models.TextField()),
            ],
            options={
                'db_table': 'news_entry',
            },
        ),
        migrations.CreateModel(
            name='player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('team', models.CharField(max_length=512)),
            ],
            options={
                'db_table': 'players',
            },
        ),
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=512)),
                ('name2', models.CharField(max_length=512)),
                ('joined', models.CharField(max_length=256)),
                ('area', models.CharField(max_length=1024)),
                ('arena', models.CharField(max_length=1024)),
            ],
            options={
                'db_table': 'teams',
            },
        ),
    ]
