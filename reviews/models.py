from django.db import models
from items.models import Item, Category
from commissions.models import Commissions
from django.contrib.auth.models import User


class Review(models.Model):
    """ Review model """

    user = models.ForeignKey(User, null=True, blank=True,
                             on_delete=models.CASCADE)
    item = models.ForeignKey(Item, null=True, blank=True,
                             on_delete=models.CASCADE)
    commission = models.ForeignKey(Commissions, null=True, blank=True,
                                   on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    body = models.TextField(max_length=500)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    featured = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True, blank=False, null=False)

    class Meta:
        """ Meta class for Review model """
        ordering = ['-date']

    def __str__(self):
        return f"{self.title}"
