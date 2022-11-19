from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.CharField(max_length=100)
    type = models.ManyToManyField("core.Type", null=True, blank=True)

    def __str__(self):
        return self.name


class Type(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title
