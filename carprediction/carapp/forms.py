from django import forms
import datetime

# Choices for the year field
YEAR_CHOICES = [(str(year), str(year)) for year in range(1990, datetime.date.today().year + 1)]

# Choices for the currency field


class CarInputForm(forms.Form):
    year = forms.ChoiceField(
        choices=[('default', 'Select Year of Manufacture')] + YEAR_CHOICES,
        label='Year of Manufacture',
    )
    kilometer_driven = forms.IntegerField(label='Kilometer Driven')

    FUEL_CHOICES = [
        ('default', 'Select Fuel Type of The Car'),
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('CNG', 'CNG'),
    ]
    fuel_type = forms.ChoiceField(
        choices=FUEL_CHOICES,
        label='Fuel Type',
    )

    SELLER_CHOICES = [
        ('default', 'Select Seller Type of The Car'),
        ('Dealer', 'Dealer'),
        ('Individual', 'Individual'),
    ]
    seller_type = forms.ChoiceField(
        choices=SELLER_CHOICES,
        label='Seller Type',
    )

    TRANSMISSION_CHOICES = [
        ('default', 'Select Transmission Type of The Car'),
        ('Manual', 'Manual'),
        ('Automatic', 'Automatic'),
    ]
    transmission = forms.ChoiceField(
        choices=TRANSMISSION_CHOICES,
        label='Transmission',
    )

 

    present_price = forms.DecimalField(
        label='Present Price',
        widget=forms.TextInput(attrs={'placeholder': 'Enter the amount'}),
    )
