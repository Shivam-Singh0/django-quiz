from email.policy import default
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Question(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    question = models.CharField(max_length=200, null=True)
    op1 = models.CharField(max_length=200, null=True)
    op2 = models.CharField(max_length=200, null=True)
    op3 = models.CharField(max_length=200, null=True)
    op4 = models.CharField(max_length=200, null=True)
    ans = models.CharField(max_length=200, null=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.question


class Score(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)
    score = models.IntegerField(default=0)
    correct = models.IntegerField(default=0)
    incorrect = models.IntegerField(default=0)
