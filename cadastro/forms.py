from django import forms
from .models import EmailCliente
import datetime
'''
class EmailForm(forms.ModelForm):
	class Meta:
		model = EmailCliente
		fields = [
			'nome',
			'contato',
			'dia',
			'hora'
		]
'''

class EmailForm(forms.ModelForm):
	nome = forms.CharField(label='Seu nome:', widget=forms.TextInput(attrs={'placeholder': 'João da Silva'}))
	contato = forms.EmailField(label='Seu e-mail:', widget=forms.EmailInput(attrs={'placeholder': 'seu_email@email.com'}))
	dia = forms.DateField(label='Dia:', input_formats=['%d/%m/%Y', '%d/%m/%y'], widget=forms.DateInput(attrs={'placeholder': '24/11/2019'}))
	hora = forms.TimeField(label='Hora:', input_formats=['%H:%M'], widget=forms.TimeInput(attrs={'placeholder': '16:15'}))
	class Meta:
		model = EmailCliente
		fields = [
			'nome',
			'contato',
			'dia',
			'hora'
		]
	