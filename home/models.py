from django.db import models
from django.contrib.auth.models import User

class arithmeticNotesAnswers(models.Model):
    answer = models.FloatField(null=True)

class arithmeticUserAnswer(models.Model):
    answer = models.FloatField(null=True)

class Post(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()

    def __str__(self):
        return self.title


    
