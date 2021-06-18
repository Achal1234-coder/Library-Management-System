from django.db import models


class Books(models.Model):
    ''' Create a model Books '''

    book_name = models.CharField(max_length=20)
    author = models.CharField(max_length=30)
    book_id = models.IntegerField()
    no_of_book = models.IntegerField()
    image_of_book = models.ImageField(upload_to='images/')
