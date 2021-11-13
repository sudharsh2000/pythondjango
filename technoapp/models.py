from django.db import models

# Create your models here.
from django.urls import reverse


class categ(models.Model):
    name=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
    def get_url(self):
        return reverse('home2',args=[self.slug])

class mobiles(models.Model):
    mobname=models.CharField(max_length=200,unique=True)
    slug=models.SlugField(max_length=200,unique=True)
    img=models.ImageField(upload_to='photos')
    desc=models.TextField()
    price=models.IntegerField()
    stock=models.IntegerField()
    availability=models.BooleanField()
    category=models.ForeignKey(categ,on_delete=models.CASCADE)
    def __str__(self):
        return '{}'.format(self.mobname)

    def get_url2(self):
        return reverse('mobilehome', args=[ self.slug ])