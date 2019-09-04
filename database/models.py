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
