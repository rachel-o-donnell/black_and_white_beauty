from django import forms
from .widgets import CustomClearableFileInput
from .models import Review


class ReviewForm(forms.ModelForm):
    """ Create form based on Review model """

    class Meta:
        model = Review
        exclude = ('user', 'image_url')

    image = forms.ImageField(required=False, widget=CustomClearableFileInput)
    featured = forms.BooleanField(
        label="Click here if you would like your review to be featured",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'One word description',
            'body': 'Go on, give us some more detail...',
        }

        for field in self.fields:
            if field != 'image' and field != 'featured' and field != 'item' and field != 'commission':  # noqa
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
