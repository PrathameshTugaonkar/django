from django import forms
from .models import  Trial


class ContactForm(forms.Form):
	name= forms.CharField()
	email= forms.EmailField(label='E-mail')
	category = forms.ChoiceField(choices=[('question', 'Question'), ('other', 'Other')])
	subject = forms.CharField(required=False)
	body=forms.CharField(widget=forms.Textarea)

class SnippetForm(forms.ModelForm):
	class Meta:
		model= Trial
		fields = ('name','body','email','city','profile_image')