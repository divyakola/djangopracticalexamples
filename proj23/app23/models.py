from django.db import models

# Create your models here.
class EmployeModel(models.Model):
    eid=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=30)
    esal=models.DecimalField(max_digits=6,decimal_places=2)
    edno=models.IntegerField()
