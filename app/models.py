from django.db import models

# Create your models here.


class Order(models.Model):
    #slug = models.SlugField(max_length=200, unique=True, default=uuid.uuid1)
    name = models.CharField(max_length=100, unique=False)
    email = models.CharField(max_length=100, unique=True)
    comment = models.TextField(max_length=2000, unique=False)

