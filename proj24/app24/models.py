from django.db import models

# Create your models here.
class customer(models.Model):
    cid=models.IntegerField(primary_key=True)
    cname=models.CharField(max_length=20)
    cadd=models.CharField(max_length=30)
    payment=models.DecimalField(max_digits=5,decimal_places=2)
    