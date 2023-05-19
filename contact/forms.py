from django import forms
from .widgets import CustomClearableFileInput
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Form class for the contact form
    """
    class Meta:
        model = Contact
        fields = '__all__'

    image = forms.ImageField(
        label='Add a pic below if its relevent to your query', required=False,
        widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and remove auto-generated
        labels
        """
        super().__init__(*args, **kwargs)

        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'enquiry_subject': 'Reason for contacting',
            'body': 'We welcome your enquiry!'
                    ' Please attach a photo below if relevent',
            'image_url': 'Current image',
            'image': 'If relevent',
            'order_number': 'If relevent',
            'dimensions': 'If relevent',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
