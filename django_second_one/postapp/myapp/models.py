from django.db import models

class Entry(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    content = models.TextField()

    def __str__(self):
      return F'{self.title} {self.date}'