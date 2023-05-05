from django.db import models


class Contact(models.Model):
    """
    A model to allow site users to contact the site owner
    """
    CHOICES = (
        ('Commissions', 'Commissions'),
        ('Complaint', 'Complaint'),
        ('Orders', 'Orders'),
        ('Returns', 'Returns'),
        ('Other', 'Other'),
    )
    full_name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    enquiry_subject = models.CharField(max_length=20,
                                       null=False, blank=False, choices=CHOICES)
    order_number = models.CharField(max_length=32, null=True, blank=True)
    body = models.TextField(max_length=1000, null=False, blank=False)
    dimensions = models.CharField(max_length=20, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.full_name
