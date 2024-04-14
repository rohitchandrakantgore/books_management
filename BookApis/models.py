from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    no_of_pages = models.IntegerField()
    author = models.CharField(max_length=100)
    publisher_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name