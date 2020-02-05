from django.db import models


class Card(models.Model):
    title = models.CharField(max_length=20)
    term_length = models.CharField(max_length=15)
    description = models.TextField()
    rate = models.FloatField()
