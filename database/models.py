from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length = 255)
    published = models.DateTimeField()
    source = models.CharField(max_length = 255)
    image = models.URLField()
    content_raw = models.TextField()
    content_display = models.TextField()
    class Meta:
        app_label = 'database'
        db_table = 'news'

class Team(models.Model):
    full_name = models.CharField(max_length = 255, unique = True)
    short_name = models.CharField(max_length = 255)
    full_en_name = models.CharField(max_length = 255)
    joined = models.CharField(max_length = 255)
    area = models.CharField(max_length = 255)
    arena = models.CharField(max_length = 255)
    class Meta:
        app_label = 'database'
        db_table = 'teams'

class Player(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    full_name = models.CharField(max_length = 255)
    team = models.ForeignKey('Team', on_delete = models.CASCADE)
    class Meta:
        app_label = 'database'
        db_table = 'players'

class Relation(models.Model):
    news = models.ForeignKey('News', on_delete = models.CASCADE)
    team = models.ForeignKey('Team', on_delete = models.CASCADE)
    class Meta:
        app_label = 'database'
        db_table = 'relation'
