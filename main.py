from selenium import webdriver
from Classes.ConfigNavegador import Navegador
from Classes.AbrirConversas import Conversa
from time import sleep
import emoji

opcao_mensagem = ''
ultima_mensagem = None

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
#escrever_mensagem.enviar_mensagem('''Olá, me chamo Beta, à assistente virtual da Rô.
#Essas são algumas opções disponíveis para interação comigo.
#1- Tabela de preços.
#2- Agendamento de horários.
#3- Falar diretamente com a Rô.
#4- Finalizar Atendimento.''')
escrever_mensagem.enviar_mensagem_inicial()
# Leitura da opção da pessoa.
while True:
    sleep(5)
    opcao_mensagem = escrever_mensagem.ler_mensagem().strip()

    if opcao_mensagem and opcao_mensagem != ultima_mensagem:
        ultima_mensagem = opcao_mensagem

        if opcao_mensagem == '1':
            escrever_mensagem.enviar_mensagem('Tabela de preços')
            escrever_mensagem.enviar_mensagem('Posso lhe ajudar com mais alguma coisa?')

        elif opcao_mensagem == '2':
            escrever_mensagem.enviar_mensagem('Agendamento de horários')
            escrever_mensagem.enviar_mensagem('Posso lhe ajudar com mais alguma coisa?')

        elif opcao_mensagem == '3':
            escrever_mensagem.enviar_mensagem('Esse é o link para falar diretamente com a Rô: https://tinyurl.com/RobertaFrancaDesigner')
            escrever_mensagem.enviar_mensagem('Posso lhe ajudar com mais alguma coisa?')

        elif opcao_mensagem == '4':
            escrever_mensagem.enviar_mensagem('''Atendimento finalizado com sucesso. Espero ter ajudado em tudo que você precisava. 
Obrigado por confiar no trabalho da Rô. 🥰❤️
Nos vemos em breve. 🤭''')
            break

    else:
        escrever_mensagem.enviar_mensagem('Opção Inválida, escolha uma das opções válidas.')
    
        escrever_mensagem.enviar_mensagem('''Por favor, escolha uma destas opções para interagir comigo:
1- Tabela de Preços.
2- Agendamento de horários.
3- Falar diretamente com a Rô.
4- Finalizar Atendimento.''')
    sleep(5)