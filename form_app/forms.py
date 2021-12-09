from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    email = forms.EmailField(max_length=50)
    text = forms.CharField(widget=forms.Textarea)