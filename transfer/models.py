from django.db import models
class transactions(models.Model):
    seller=models.CharField(max_length=65)
    buyer=models.CharField(max_length=65)
    price=models.IntegerField()
    code=models.CharField(max_length=65, default="7890")

