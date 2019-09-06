from django.http import HttpResponse
def ClimaAgora(request):
	return HttpResponse("https://api.openweathermap.org/data/2.5/weather?id=3394023&APPID=9e70fbffdde1b3cfcb57ddd5f3a250b4")
	#Tirar a minha chave daqui e colocar em um arquivo com .gitignore

def Clima5dias(request):
	return HttpResponse("https://api.openweathermap.org/data/2.5/forecast?id=3394023&APPID=9e70fbffdde1b3cfcb57ddd5f3a250b4")
	#Tirar a minha chave daqui e colocar em um arquivo com .gitignore