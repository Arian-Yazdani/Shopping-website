from django.db import models


class Products(models.Model):
    title = models.CharField(max_length=100)
    description =models.TextField()
    price = models.PositiveIntegerField()
    cover = models.ImageField(upload_to='covers',blank=True,null=True)
