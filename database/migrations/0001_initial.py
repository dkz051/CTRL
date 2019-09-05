# Generated by Django 2.2.5 on 2019-09-04 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('published', models.DateTimeField()),
                ('source', models.TextField()),
                ('image', models.TextField()),
                ('content', models.TextField()),
            ],
        ),
    ]