import smtplib
from leitor import climanow, prevhoje
def mandaemail(nome, contato, dia, hora):
	meu_email = #email here
	minha_s = #password here
	climatual = climanow()
	prevclima = prevhoje()


	with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.ehlo()

		smtp.login(meu_email, minha_s)

		assunto = 'Alerta climático'
		corpo = 'Olá, {}!\n Esta é a previsão para o Parque das Dunas após seu alerta({} - {}):\n Clima Atual -> {}.\n Previsão -> {}.\n Esperamos que tenha uma boa trilha!\n Equipe ClimaTempo'.format(nome, dia, hora, climatual, prevclima)

		mensagem = f'Subject: {assunto}\n\n{corpo}'

		smtp.sendmail( meu_email, contato, mensagem.encode('utf-8'))

# mandaremail("Daniel", "dhcp2013@gmail.com", "hoje2", "agora2")
