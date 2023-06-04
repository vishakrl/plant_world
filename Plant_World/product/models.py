from django.db import models

# Create your models here.
class plant(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to='pic')
    price=models.IntegerField()
    qty=models.IntegerField()
    desc=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
