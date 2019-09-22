from django import forms

class NameForm(forms.Form):
    urlink = forms.CharField(label="Article link",widget=forms.TextInput(
        attrs={
            'class':'form-control form-control-sm type-txt',
        }
    ))
