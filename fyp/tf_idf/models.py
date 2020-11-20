from django.db import models

# Create your models here.

class Papers(models.Model):
    paper_id=models.IntegerField()
    paper_title=models.CharField(max_length=(200))
    author_keywords=models.CharField(max_length=(200))
    abstract=models.CharField(max_length=(2000))
    area=models.CharField(max_length=(150))
