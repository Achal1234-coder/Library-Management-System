from django.db import models

''' Make a model named RegistrationStudent '''
class RegistrationStudent(models.Model):
    student_Name = models.CharField(max_length=30)
    student_Id = models.IntegerField()
    password = models.CharField(max_length=20)
