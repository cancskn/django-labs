from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        print(self.name)
        return f"Name: {self.name}"