from django.db import models


class RegistrationStudent(models.Model):
    ''' Make a model named RegistrationStudent '''

    student_name = models.CharField(max_length=30)
    student_id = models.IntegerField()
    password = models.CharField(max_length=20)
