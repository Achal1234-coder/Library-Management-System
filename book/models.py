from django.db import models


class Books(models.Model):
    book_name = models.CharField(max_length=20)
    writter = models.CharField(max_length=30)
    published_year = models.DateField()
    no_of_book = models.IntegerField()
    image_of_book = models.ImageField(upload_to='book/image', blank=True)
