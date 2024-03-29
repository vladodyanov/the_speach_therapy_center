from django import forms


class ContactForm(forms.Form):
    MAX_NAME_LENGTH = 250

    name = forms.CharField(
        max_length=MAX_NAME_LENGTH
    )

    email = forms.EmailField()

    message = forms.CharField(
        widget=forms.Textarea
    )
