from django.db import models


class IssueBook(models.Model):
    student_name = models.CharField(max_length=30)
    book_name = models.CharField(max_length=20)
    book_id = models.IntegerField()
