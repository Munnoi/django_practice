from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    age = models.IntegerField()

    class Departments(models.TextChoices):
        CSE = "cse", "CSE"
        EEE = "eee", "EEE"
        ECE = "ece", "ECE"
        ICE = "ice", "ICE"
    department = models.CharField(
        max_length=3,
        choices=Departments.choices
    )
    
    date_joined = models.DateField()

    def __str__(self):
        return self.name + ' ' + self.department
