from django.db import models

# Create your models here.
class Company(models.Model):
    cname=models.CharField(max_length=20)
    cadd=models.CharField(max_length=30)
    class Meta:
        abstract=True

class Employe(Company):
    eid=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=20)
    def __str__(self):
        return "%d %s %s %s"%(self.eid,self.ename,self.cname,self.cadd)

    
