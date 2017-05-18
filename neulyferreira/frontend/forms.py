from django import forms

# our new form
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    contact_cellphone = forms.CharField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
