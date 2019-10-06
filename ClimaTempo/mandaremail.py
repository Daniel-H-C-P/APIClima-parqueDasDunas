import smtplib

meu_email = 'climatemponatal@gmail.com'
minha_s = 'IFRn2019'

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.ehlo()

	smtp.login(meu_email, minha_s)

	assunto = 'texte de email'
	corpo = 'Email automático enviado'

	mensagem = f'Subject: {assunto}\n\n{corpo}'

	smtp.sendmail( meu_email, meu_email, mensagem.encode('utf-8'))
