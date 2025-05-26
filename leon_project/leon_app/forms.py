from django import forms
from .models import Feedback, Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'message']

    def save(self, commit=True):
        user = super().save(commit)
        message = self.cleaned_data.get('message')
        if commit:
            Profile.objects.update_or_create(user=user, defaults={'message': message})
        return user