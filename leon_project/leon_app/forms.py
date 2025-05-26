from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'text']
        labels = {
            'name': "Name",
            'text': "Your feedback"
        }
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name'}),
            'text': forms.Textarea(attrs={'placeholder': 'Your feedback'}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)