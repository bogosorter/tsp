from django.db import models

class Submission(models.Model):
    name = models.CharField(max_length=40)
    score = models.FloatField()
