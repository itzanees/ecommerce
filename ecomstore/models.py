from django.db import models

# Create your models here.

class Category(models.Model):
    cat_code = models.IntegerField(unique=True, default='')
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        catName = str(self.cat_code) +'-' + self.name
        return catName


class Product(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity =models.IntegerField()
    price =  models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
