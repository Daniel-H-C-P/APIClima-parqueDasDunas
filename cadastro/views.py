from django.shortcuts import render, redirect
from .forms import EmailForm


def cadastro_pedidos(request):
	form = EmailForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('http://127.0.0.1:8000/ClimaParque3/') #vou ter de mudar isso-> CRIAR PÁGINA DE 'CADASTRO CONCLUÍDO!'
	contexto = {
		'form': form,
		
	}

	return render (request, "../templates/formulario.html", contexto)
# Create your views here.
