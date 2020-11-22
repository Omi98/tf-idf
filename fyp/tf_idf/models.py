from django.db import models

# Create your models here.

class Papers(models.Model):
    paper_id=models.IntegerField()
    paper_title=models.CharField(max_length=(200))
    author_keywords=models.CharField(max_length=(200))
    abstract=models.CharField(max_length=(2000))
    area=models.CharField(max_length=(150))

class RecommendationModel(models.Model):
    word=models.CharField(max_length=(200))
    tfidf=models.DecimalField(max_digits=(15), decimal_places=(15))
    paper_id=models.IntegerField(max_length=(200))
