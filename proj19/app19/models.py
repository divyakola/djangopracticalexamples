from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Owner(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return "%s"%self.name
class Car(models.Model):
    cnumber=models.IntegerField(primary_key=True)    
    cbrand=models.CharField(max_length=30)
    ctype=models.CharField(max_length=20)
    cowner=models.ForeignKey(Owner,on_delete=models.CASCADE)
    def __str__(self):
        return "cnumber:%d,cbrand:%s,ctype:%s,cowner:%s"%(self.cnumber,self.cbrand,self.ctype,self.cowner)
        

