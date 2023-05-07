""" faq forms.py"""
from django import forms
from .models import Faq


class FaqForm(forms.ModelForm):
    """ FAQ's form """
    class Meta:
        """ faq form"""
        model = Faq
        fields = '__all__'
