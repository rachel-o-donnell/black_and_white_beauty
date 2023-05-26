from django import forms
from .widgets import CustomClearableFileInput
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Form class for the contact form
    """
    class Meta:
        model = Contact

        exclude = ('image_url',)

    image = forms.ImageField(required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """Add placeholders and remove auto-generated labels """
        super().__init__(*args, **kwargs)

        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'body': 'We welcome your enquiry!'
                    ' Please attach a photo below if relevent',
            'order_number': 'If relevent',
            'dimensions': 'If relevent',
        }

        for field in self.fields:
            if field != 'image' and field != 'enquiry_subject':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
