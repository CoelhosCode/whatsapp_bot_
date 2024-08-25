from selenium import webdriver
from Classes.ConfigNavegador import Navegador
from Classes.AbrirConversas import Conversa
from time import sleep
from selenium.webdriver.common.keys import Keys
import emoji

opcao_mensagem = ''

# Inciando o navegador FireFox.
navegador = Navegador()
driver = navegador.configuracao_navegador()

# Tempo de espera para ler o QR CODE
input('Pressione Enter após escanear o QR CODE!')

# Abrir a primeira conversa que tiver uma notificação
while True:
    conversa = Conversa(driver)
    conversa.selecionar_conversa()

    # Escrever a mensagem de Saudação
    escrever_mensagem = Conversa(driver)
    escrever_mensagem.enviar_mensagem_inicial()
    
    ultima_mensagem = None

    # Leitura da opção da pessoa.
    while True:
        sleep(5)
        opcao_mensagem = escrever_mensagem.ler_mensagem()

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
                conversa.sair_conversa()
                break