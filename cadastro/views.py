from django.shortcuts import render
from .forms import EmailForm

def cadastro_pedidos(request):
	form = EmailForm(request.POST or None)
	if form.is_valid():
		form.save()
	contexto = {
		'form': form

	}

	return render (request, "../templates/formulario.html", contexto)
# Create your views here.
