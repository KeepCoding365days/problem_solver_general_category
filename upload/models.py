from django.db import models

# Create your models here.
class upload(models.Model):
    name=models.CharField(max_length=64)
    category=models.CharField(max_length=64)
    price=models.IntegerField()
    code=models.CharField(max_length=64)
    origin=models.CharField(max_length=64)
    previous_owner=models.CharField(max_length=64, default=origin)
    new_owner=models.CharField(max_length=64 )
    new_price=models.IntegerField(null=True)
    for_sale=models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"