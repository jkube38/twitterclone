from django import forms


# Create Tweet Form
class NewTweetForm(forms.Form):
    body = forms.CharField(widget=forms.Textarea)
