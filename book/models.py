from django.db import models


class Books(models.Model):
    Book_Name = models.CharField(max_length=20)
    Writter = models.CharField(max_length=30)
    Published_Year = models.DateField()
    No_of_Book = models.IntegerField()
    Image_of_Book = models.ImageField(upload_to='book/image', blank=True)
