from django import forms


class homeform(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
      attrs={
          'class': 'form-control',
          'placeholder': 'SEARCH FOR A COUNTRY',

      }
    ))
    checkbox = forms.BooleanField

