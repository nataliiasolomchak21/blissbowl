from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user', 'favourite_bowls']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders.get(field, field)} *'
            else:
                placeholder = placeholders.get(field, field)

            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = ('border-black'
                                                        'rounded-2 '
                                                        'profile-form-input')
            self.fields[field].label = False
