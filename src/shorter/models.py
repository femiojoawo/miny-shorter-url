from django.db import models

# Create your models here.
class ShortUrl(models.Model):
    true_url = models.URLField(blank=False)
    short_suffix = models.CharField(blank=False)
    num_use = models.PositiveIntegerField(default=0,blank=True)
