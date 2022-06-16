from django.db import models
from django.core.validators import FileExtensionValidator

class Author(models.Model):
    name = models.CharField(max_length=100)


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=60,null=True,blank=True)
    country = models.CharField(max_length=50,null=True,blank=True)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ForeignKey(Author, on_delete=models.CASCADE,null=True,blank=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE,null=True,blank=True)
    published = models.DateField()
    book_img = models.ImageField(upload_to='book_images/',null=True,blank=True)
    pdf_file = models.FileField(upload_to='book_pdf/',validators=[FileExtensionValidator(['pdf'])])

