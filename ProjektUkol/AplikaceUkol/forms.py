from django import forms

class CommentForm(forms.Form):
    name = forms.CharField(max_length=100, label="Vaše jméno")
    rating = forms.IntegerField(min_value=1, max_value=10, initial=5, label="Vaše hodnocení")
    comment = forms.CharField(label="Váš komentář")