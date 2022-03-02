from django.db import models

# Create your models here.
class Thief(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return "%s"%self.name
class Car(models.Model):
    cnumber=models.IntegerField(primary_key=True)    
    cbrand=models.CharField(max_length=30)
    ctype=models.CharField(max_length=20)
    cthief=models.ManyToManyField(Thief)
    def __str__(self):
        return "cnumber:%d,cbrand:%s,ctype:%s"%(self.cnumber,self.cbrand,self.ctype)
        

