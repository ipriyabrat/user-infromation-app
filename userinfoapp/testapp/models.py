
from django.db import models
from django.contrib.auth.models import User
 

# Create your models here.

class UserInfo(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=300)
    mobileno=models.IntegerField()
    email=models.EmailField()
    blood_group=models.CharField(max_length=20)
    Identity_card_number=models.IntegerField()
    driving_licence_no=models.CharField(max_length=20)
    bank_ac_no=models.IntegerField()
    creditcard_no=models.IntegerField()
    atmcard_no=models.IntegerField()
    user=models.ForeignKey(User, on_delete= models.CASCADE)
    # user_image=models.ImageField(upload_to='profileimg',blank=True)
    date=models.DateTimeField(auto_now_add=True)





