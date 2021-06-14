from django.db import models

''' Make a model named RegistrationStudent '''
class RegistrationStudent(models.Model):
    Student_Name = models.CharField(max_length=30)
    Student_Id = models.IntegerField()
    Password = models.CharField(max_length=20)
