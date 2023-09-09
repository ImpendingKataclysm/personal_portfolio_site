from django import forms
from . import models


class ReservationForm(forms.ModelForm):
    """
    Models the Reservation Form based on the Reservation DB model.
    """
    party_name = forms.CharField(
        max_length=models.NAME_MAX_LEN,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter the name of your party',
        }),
    )

    party_size = forms.IntegerField(
        max_value=100,
        required=True,
    )

    phone = forms.CharField(
        max_length=models.MAX_NUM,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your phone number',
        }),
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Your email address',
        }),
    )

    location = forms.ModelChoiceField(
        queryset=models.Location.objects.order_by('city'),
        widget=forms.RadioSelect,
        required=True,
    )

    date = forms.DateField(
        widget=forms.DateInput(attrs={
            'type': 'date',
        }),
    )

    time = forms.TimeField(
        widget=forms.TimeInput(attrs={
            'type': 'time',
        }),
    )

    class Meta:
        model = models.Reservation
        fields = (
            'party_name',
            'party_size',
            'phone',
            'email',
            'location',
            'date',
            'time',
        )
