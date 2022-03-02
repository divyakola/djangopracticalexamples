from django.db import models

# Create your models here.
class Driver(models.Model):
    dname=models.CharField(max_length=20)
    def __str__(self):
        return "Driver Name:%s"%self.dname
class Car(models.Model):
    cnumber=models.IntegerField(primary_key=True)    
    cbrand=models.CharField(max_length=30)
    ctype=models.CharField(max_length=20)
    cdriver=models.OneToOneField(Driver,on_delete=models.CASCADE)
    def __str__(self):
        return "cnumber:%d,cbrand:%s,ctype:%s,cdriver:%s"%(self.cnumber,self.cbrand,self.ctype,self.cdriver)
        
