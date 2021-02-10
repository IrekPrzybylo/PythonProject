from django import forms

from .validators import validate_url

# form to validate and save to db shortened link
class SubmitUrlForm(forms.Form):
    url = forms.CharField(
        label='',
        validators=[validate_url],
        widget = forms.TextInput(
            attrs={"placeholder": "Long URL",
                   "class": "form-control"
                   }
        )
    )


