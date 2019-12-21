from django.core.validators import MinLengthValidator, int_list_validator
from django.db import models
from django import forms


# # Create your models here.

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    Surname = models.CharField(max_length=100, default='Patel')
    Name = models.CharField(max_length=100)
    file = models.FileField(upload_to="sk/images")
    Percentage = models.FloatField(max_length=6)
    Std = models.CharField(max_length=15, default="")
    Mo_No = models.CharField(verbose_name="Phone number", max_length=10,
                             validators=[int_list_validator(sep=''), MinLengthValidator(10), ])

    objects = models.Manager()

    def __str__(self):
        return self.Name
