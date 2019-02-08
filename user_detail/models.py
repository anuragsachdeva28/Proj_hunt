from django.db import models
from django.contrib.auth import get_user_model


User=get_user_model()
# Create your models here.
class Profile(models.Model):
    leader=models.ForeignKey(User,on_delete=models.CASCADE)
    leadername=models.CharField(max_length=100)
    participant2=models.CharField(null=True,max_length=100)
    participant3=models.CharField(null=True,max_length=100)
    email1=models.EmailField()
    email2=models.EmailField(null=True)
    email3=models.EmailField(null=True)
    branch1=models.CharField(max_length=100)
    branch2=models.CharField(null=True,max_length=100)
    branch3=models.CharField(null=True,max_length=100)
    contact1=models.IntegerField()
    contact2=models.IntegerField(null=True)
    contact3=models.IntegerField(null=True)
    level=models.IntegerField(default=0)


    def __str__(self):
        return self.leadername

