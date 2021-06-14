from django.db import models

class RegistrationStudent(models.Model):
    ''' Make a model named RegistrationStudent '''

    student_Name = models.CharField(max_length=30)
    student_Id = models.IntegerField()
    password = models.CharField(max_length=20)
