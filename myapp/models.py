from django.db import models


# Create your models here.
class StudentsModel(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.first_name + '' + self.last_name


class StudentDetailsModel(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=12)
    address = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.BooleanField(max_length=10, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Others')], default='M')

    class Meta:
        db_table = 'Students'