from selenium import webdriver
from ConfigNavegador import Navegador
from AbrirConversas import Conversa
from time import sleep
import emoji

opcao_mensagem = ''

# Inciando o navegador FireFox.
navegador = Navegador()
driver = navegador.configuracao_navegador()

# Tempo de espera para ler o QR CODE
input('Pressione Enter após escanear o QR CODE!')

# Abrir a primeira conversa que tiver uma notificação
conversa = Conversa(driver)
conversa.selecionar_conversa()

# Escrever a mensagem de Saudação
escrever_mensagem = Conversa(driver)
escrever_mensagem.enviar_mensagem('''Olá, me chamo Beta, à assistente virtual da Rô.
Essas são algumas opções disponíveis para interação comigo.
1- Tabela de preços.
2- Agendamento de horários.
3- Falar diretamente com a Rô.
4- Finalizar Atendimento.''')

# Leitura da opção da pessoa.
while opcao_mensagem != 4:
    sleep(2)
    opcao_mensagem = Conversa(driver)
    opcao_mensagem.ler_mensagem()
    if opcao_mensagem == 1:
        escrever_mensagem.enviar_mensagem('Tabela de preços')
    elif opcao_mensagem == 2:
        escrever_mensagem.enviar_mensagem('Agendamento de horários')
    elif opcao_mensagem == 3:
        escrever_mensagem.enviar_mensagem('Esse é o link para falar diretamente com a Rô: https://w.app/RFNailsDesigner')
    elif opcao_mensagem == 4:
        print('''Atendimento finalizado com sucesso. Espero ter ajudado em tudo que você precisava. 
              Obrigado por confiar no trabalho da Rô. 🥰❤️
              Nos vemos em breve. 🤭''')