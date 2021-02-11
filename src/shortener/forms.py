from django import forms

from .validators import validate_url


class SubmitUrlForm(forms.Form):
    """
    Form to validate and submit URL to base to shorten it
    """
    url = forms.CharField(
        label='',
        validators=[validate_url],
        widget=forms.TextInput(
            attrs={"placeholder": "Long URL",
                   "class": "form-control"
                   }
        )
    )


