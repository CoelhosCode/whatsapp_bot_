<h1 align="center"> WhatsAppBot para Interação com Clientes.  </h1>

![Imagem Bot](https://github.com/user-attachments/assets/28e1c3ab-07af-46aa-bc5e-52928ebc7fac)
![Badge de linceça MIT](https://img.shields.io/badge/License-MIT-green) ![Badge de Desenvolvimento](https://img.shields.io/badge/Status-EM%20DESENVOLVIMENTO-GREEN)

## Descrição Do Projeto
O objetivo do projeto é automatizar o atendimento ao cliente por meio do WhatsApp.

## Status do Projeto
<h4 align="center"> 
    :construction:  Projeto em construção  :construction:
</h4>

## :hammer: Funcionalidades e Demonstração da Aplicação
### 1. Interação com cliente
Nesta fase, cabe ao bot verificar se há novas mensagens publicadas no WhatsApp, selecionar a conversa e interagir com o cliente conforme as suas necessidades.

### 2. Agendamento
Esta etapa ainda esta em desenvolvimento, mas após a sua conlusão a pessoa será capaz ver horários disponíveis na agenda e marcar horários de acordo com sua escolha diretamente no Google Agenda.

## 🛠️ Execução do Projeto
Para a execução, será necessário seguir estes passos.
1. **Execute o script:** Execute o script principal para que as funções de interação e agendamento funcionem.
2. **Escaneamento do QR CODE:** Será necessário escanear o QR CODE do WhatsApp manualmente.


## ✔️ Tecnologias Utilizada
- Selenium
- Python 3
- API do Google Calendar

## 💻 Exemplo de Uso:
```python
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
