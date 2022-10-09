from django.db import models

class arithmeticNotesAnswers(models.Model):
    answer = models.CharField(max_length=200)