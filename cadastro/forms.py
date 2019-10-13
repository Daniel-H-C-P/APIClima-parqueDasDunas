from django import forms
from .models import EmailCliente

class EmailForm(forms.ModelForm):
	class Meta:
		model = EmailCliente
		fields = [
			'nome',
			'contato',
			'dia',
			'hora'
		]