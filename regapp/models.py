from django.db import models

class suserreg(models.Model):
    First_name=models.CharField( max_length=50)
    Last_name=models.CharField( max_length=50)
    Sclass=models.CharField( max_length=50)
    Schoolname=models.CharField( max_length=50)
    board=models.CharField( max_length=50)
    phone_no=models.CharField( max_length=50)
    

     