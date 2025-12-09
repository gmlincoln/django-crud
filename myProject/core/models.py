from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.IntegerField()
    full_name = models.TextField(max_length=150)
    department = models.TextField(max_length=100)
    dob = models.DateField()
    gender = models.TextField(max_length=20)
    address = models.TextField(max_length=200)
    
    def __str__(self):
        
        return f"{self.student_id} - {self.full_name}"
    
    