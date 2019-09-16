from django import forms

class NameForm(forms.Form):
    urlink = forms.CharField(label='Article Link', max_length=100)