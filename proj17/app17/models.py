from django.db import models

# Create your models here.
class Student(models.Model):
    sid=models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=20)
    sadd=models.CharField(max_length=30)
    sfee=models.DecimalField(max_digits=6,decimal_places=2)
    sstatus=models.BooleanField(default=False)
    
