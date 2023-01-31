from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Drones(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100)
    img_large=models.ImageField(upload_to='Pics')
    img_small=models.ImageField(upload_to='Pics', default='Pictures')
    desc=models.TextField()

    class Meta:
        ordering=('name',)
        verbose_name='Drone'
        verbose_name_plural='Drones'

    def __str__(self):
        return '{}'.format(self.name)

class Interactions(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100)
    img_large=models.ImageField(upload_to='Pics')
    img_small=models.ImageField(upload_to='Pics', default='Pictures')
    desc=models.TextField()

    class Meta:
        ordering=('name',)
        verbose_name='Interaction'
        verbose_name_plural='Interactions'

    def __str__(self):
        return '{}'.format(self.name)

class Services(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100)
    img_large=models.ImageField(upload_to='Pics')
    img_small=models.ImageField(upload_to='Pics', default='Pictures')
    desc=models.TextField()

    class Meta:
        ordering=('name',)
        verbose_name='Service'
        verbose_name_plural='Services'

    def __str__(self):
        return '{}'.format(self.name)


