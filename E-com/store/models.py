from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50,null=False,blank=False)
    image=models.ImageField(upload_to="images",null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0=default,Hidden")

    def __str__(self) :
        return self.name


class Product(models.Model):
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=50,null=False,blank=False)
    product_image=models.ImageField(upload_to="images",null=False,blank=False)
    description=models.CharField(max_length=500,null=False,blank=False)
    price=models.FloatField(null=False,blank=False)
    status=models.BooleanField(default=False,help_text="0=default,Hidden")

    def __str__(self):
        return self.name