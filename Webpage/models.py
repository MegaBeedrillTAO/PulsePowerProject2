from django.db import models


class Card(models.Model):
    titles = [('Power of Credit', 'Power of Credit'), ('New Fixed', 'New Fixed')]
    title = models.CharField(max_length=15, choices=titles)
    term_length = models.IntegerField()
    description = models.TextField()
    rate = models.FloatField()
