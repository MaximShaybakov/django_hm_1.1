from django.db import models
from django.urls import reverse


class Phone(models.Model):
    id = models.PositiveIntegerField(primary_key=True, verbose_name='id')
    name = models.CharField(max_length=100, verbose_name='name')
    price = models.PositiveIntegerField(verbose_name='price')
    image = models.URLField(max_length=255, verbose_name='image')
    release_date = models.DateField(auto_now=False, auto_now_add=False, verbose_name='release_date')
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=125, unique=True, null=True)

    def get_absolute_url(self):
        return reverse('phone_detail', kwargs={'slug': self.slug})
