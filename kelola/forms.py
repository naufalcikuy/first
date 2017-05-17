from django import forms
from .models import Knowledge, History, BabyBio, Event
from django.forms.extras import SelectDateWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Knowledge
        fields = ('category', 'title', 'text',)

class BabyBioForm(forms.ModelForm):	
	
    class Meta:
        model = BabyBio        
        date_birth = forms.DateField(widget=SelectDateWidget())
        fields = ('baby_name', 'jenis_kelamin', 'date_birth', 'address', 'mother_name', 'father_name', 'weight_birth', 'height_birth', 'headcircumference_birth', 'parent_email',)

class HistoryForm(forms.ModelForm):
    class Meta:
        model = History
        fields = ('baby','check', 'value', 'imun_value')

class new_event_form(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'description', 'date_event',)

class edit_member_form(forms.ModelForm):
    class Meta:
        model = BabyBio
        fields = ('id_baby', 'address',)
        excludes =('baby_name', 'date_birth', 'mother_name', 'father_name', 'weight_birth', 'height_birth', 'headcircumference_birth',)

class edit_knowledge_form(forms.ModelForm):
    class Meta:
        model = Knowledge        
        fields = ('title', 'text')

class edit_event_form(forms.ModelForm):
    class Meta:
        model = Event       
        fields = ('title', 'description', 'date_event')




