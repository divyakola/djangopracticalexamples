from django.db import models

# Create your models here.
class Customer(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=20)
    add=models.CharField(max_length=30)
    def __str__(self):
        return "id:%s,name:%s,add:%s"%(self.id,self.name,self.add)
class Student(Customer):
    class Meta:
        proxy=True
