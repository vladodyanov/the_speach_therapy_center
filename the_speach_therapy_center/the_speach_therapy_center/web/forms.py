from django import forms


class SpeachCenterContactForm(forms.Form):
    MAX_NAME_LENGTH = 250

    name = forms.CharField(
        max_length=MAX_NAME_LENGTH,
        widget=forms.TextInput(
            attrs={'placeholder': 'Please enter your name...'}),
    )

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Please enter your email...'}),
    )

    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'Please enter your message...'}),
    )


