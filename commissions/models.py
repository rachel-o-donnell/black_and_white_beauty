from django.db import models


class Commissions(models.Model):
    category = models.ForeignKey(
        'items.Category', null=True, blank=True, on_delete=models.SET_NULL)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=254)
    brief = models.CharField(max_length=1024, null=True, blank=True)
    description = models.TextField(max_length=1024)
    dimensions = models.CharField(max_length=250)

    def __str__(self):
        return self.name
