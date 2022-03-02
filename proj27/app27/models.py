from django.db import models

# Create your models here.
class College(models.Model):
    cname=models.CharField(max_length=20)
    cadd=models.CharField(max_length=30)
    def __str__(self):
        return "%s %s"%(self.cname,self.cadd)

class Student(College):
    sid=models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=20)
    sadd=models.CharField(max_length=30)
    def __str__(self):
        return "%s %s %d %s %s"%(self.cname,self.cadd,self.sid,self.sname,self.sadd)
