from django import forms
from .widgets import CustomClearableFileInput
from .models import Review

from django.contrib.auth.models import User


class ReviewForm(forms.ModelForm):
    """ Create form based on Review model """

    class Meta:
        model = Review
        exclude = ('user', 'image_url')

    image = forms.ImageField(
        label='We love seeing how you have styled your pieces in your home', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'item': 'Item name',
            'commission': 'Commission piece',
            'title': 'One word description',
            'body': 'Go on, give us some more detail...',
            'image': 'Image',
            'featured': "Please tick this if you would like your review to be published on the site"

        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
