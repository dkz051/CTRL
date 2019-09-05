from django.db import models

# Create your models here.
class news_entry(models.Model):
    title = models.CharField(max_length = 1024)
    published = models.DateTimeField()
    source = models.CharField(max_length = 2048)
    image = models.CharField(max_length = 2048)
    content = models.TextField()

    class Meta:
        app_label = 'database'
        db_table = 'news_entry'

class Team(models.Model):
    full_name = models.CharField(max_length = 512, unique = True)
    short_name = models.CharField(max_length = 512)
    full_en_name = models.CharField(max_length = 512)
    joined = models.CharField(max_length = 256)
    area = models.CharField(max_length = 1024)
    arena = models.CharField(max_length = 1024)

    class Meta:
        app_label = 'database'
        db_table = 'teams'

class Player(models.Model):
    first_name = models.CharField(max_length = 256)
    last_name = models.CharField(max_length = 256)
    full_name = models.CharField(max_length = 512)
    team = models.ForeignKey('Team', on_delete = models.CASCADE)

    class Meta:
        app_label = 'database'
        db_table = 'players'
