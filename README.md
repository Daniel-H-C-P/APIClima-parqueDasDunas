# APIClima-parqueDasDunas
Projeto de API para acompanhamento climático do Parque das Dunas (Natal/RN) feito como trabalho de conclusão de curso do técnico de Informática para Internet no Instituto Federal do Rio Grande do Norte (IFRN), com previsão de apresentação em novembro de 2019.

# Resumo
O projeto segue a linha de pesquisa de consumo de serviços/dados públicos e criação de APIs. Partindo de dados coletados na API do OpenWeather e os interpretando na busca por precipitações, pretendemos criar um serviço online de notificação de mudanças climáticas para os usuários do Parque das Dunas que pretendem fazer trilhas.

# Recursos
Nossa proposta será feita com a linguagem Python e os frameworks Django e Django Rest, fora o consumo de dados da plataforma climática OpenWeather.

# Método
Partimos da ativação de uma conta gratuita no site do OpenWeather e criamos um script que busca nessa API o clima atual e a previsão dos próximos 5 dias para Natal/RN, rodando de 10 em 10 minutos (tempo mínimo de atualização dos dados do OpenWeather). Com os dados coletados, criamos arquivos json para serem lidos e usados em nosso servidor, os atualizando em cada request do dito script. Dessa forma garantimos uma precisão de 10 minutos na página index do projeto, facilitando o planejamento de trilhas do usuário e permitindo o acompanhamento do clima quase em tempo real. Na página index ainda construímos um formulário para cadastro do usuário que deseja receber um aviso por email da previsão do clima, o formulário se comunica com o banco de dados que então é monitorado por um controlador que envia os emails no dia/horário previsto.
