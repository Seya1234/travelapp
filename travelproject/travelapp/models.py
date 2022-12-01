from django.db import models


# Create your models here.
class Place(models.Model):
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name


class Fruit(models.Model):
    f_name = models.CharField(max_length=250)
    f_img = models.ImageField(upload_to='pics')
    f_desc = models.TextField()

    def __str__(self):
        return self.f_name
