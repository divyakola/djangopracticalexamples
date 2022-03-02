from django.db import models

# Create your models here.
class emp(models.Model):
    eid=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=20)
    eadd=models.CharField(max_length=30)
    esal=models.DecimalField(max_digits=6,decimal_places=2)
    email=models.EmailField(blank=True)
    active=models.BooleanField(default=False)
    def __str__(self):
        return "Eid: %d,Ename: %s"%(self.eid,self.ename)
    
