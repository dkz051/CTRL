from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length = 255, verbose_name = '标题')
    published = models.DateTimeField(verbose_name = '原始发布时间')
    source = models.CharField(max_length = 255, verbose_name = '来源')
    image = models.URLField(verbose_name = '配图地址')
    content_raw = models.TextField(verbose_name = '原始内容')
    content_display = models.TextField(verbose_name = '文章内容（已分段）')
    url = models.URLField(verbose_name = '抓取源 URL')
    word_count = models.IntegerField(verbose_name = '词数统计')
    class Meta:
        app_label = 'database'
        db_table = 'news'

class Team(models.Model):
    full_name = models.CharField(max_length = 255, verbose_name = '全称', unique = True)
    short_name = models.CharField(max_length = 255, verbose_name = '简称')
    full_en_name = models.CharField(max_length = 255, verbose_name = '英文全称')
    joined = models.CharField(max_length = 255, verbose_name = '加入 NBA 时间')
    area = models.CharField(max_length = 255, verbose_name = '赛区')
    arena = models.CharField(max_length = 255, verbose_name = '主场')
    class Meta:
        app_label = 'database'
        db_table = 'teams'

class Player(models.Model):
    first_name = models.CharField(max_length = 255, verbose_name = '名')
    last_name = models.CharField(max_length = 255, verbose_name = '姓')
    full_name = models.CharField(max_length = 255, verbose_name = '全名')
    team = models.ForeignKey('Team', on_delete = models.CASCADE, verbose_name = '所属球队')
    class Meta:
        app_label = 'database'
        db_table = 'players'

class Relation(models.Model):
    news = models.ForeignKey('News', on_delete = models.CASCADE)
    team = models.ForeignKey('Team', on_delete = models.CASCADE)
    class Meta:
        app_label = 'database'
        db_table = 'relations'

class Word(models.Model):
    word = models.CharField(max_length = 63, unique = True)
    count = models.IntegerField() # Total count of occurrences of the keyword
    indices = models.TextField()
    class Meta:
        app_label = 'database'
        db_table = 'words'
