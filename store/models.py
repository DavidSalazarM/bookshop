from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=60)
    country = models.CharField(max_length=50)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    published = models.DateField()

