from django.db import models


class Faq(models.Model):
    """
    A model to allow site users to see fequently asked questions
    """

    question = models.CharField(max_length=1000, null=False, blank=False)
    answer = models.TextField(max_length=1000, null=False, blank=False)
    date = models.DateField(auto_now=True, editable=False)

    class Meta:
        """
        displays most recently added questions 1st
        """
        ordering = ['-date']

    def __str__(self):
        return f"{self.question}"
