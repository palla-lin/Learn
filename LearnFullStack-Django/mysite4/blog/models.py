from django.db import models

# Create your models here.
class user(models.Model):
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=32)


class article(models.Model):
    title=models.CharField(max_length=64)
    content=models.CharField(max_length=128)
    time=models.DateTimeField()
    user_id=models.ForeignKey('user',on_delete=models.CASCADE)
