from django.db import models


class question_model(models.Model):
    level=models.IntegerField(unique=True)
    title=models.CharField(max_length=200,null=True)
    description=models.TextField(null=True)
    image=models.ImageField(null=True,blank=True)
    correct_ans=models.CharField(max_length=500)


    def __str__(self):
        return self.title

