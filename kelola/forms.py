from django import forms
from .models import Knowledge

class PostForm(forms.ModelForm):
    class Meta:
        model = Knowledge
        fields = ('category','title', 'text',)