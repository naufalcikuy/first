from django import forms
from .models import Knowledge, History

class PostForm(forms.ModelForm):
    class Meta:
        model = Knowledge
        fields = ('category','title', 'text',)

class HistoryForm(forms.ModelForm):
    class Meta:
        model = History
        fields = ('check', 'value', 'imun_value')
