from django.db import models
from django.contrib.auth.models import User


class QuestionManager(models.Manager):
    def new(self):
        pass

    def popular(self):
        pass


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(null=True)
    added_at = models.DateTimeField(null=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='like')
    objects = QuestionManager()


class Answer(models.Model):
    text = models.TextField(null=True)
    added_at = models.DateTimeField(null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
