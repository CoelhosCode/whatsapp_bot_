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
from Classes.ConfigNavegador import Navegador
from Classes.AbrirConversas import Conversa
from time import sleep

# Inciando o navegador FireFox.
navegador = Navegador()
driver = navegador.configuracao_navegador()

# Tempo de espera para ler o QR CODE
input('Pressione Enter após escanear o QR CODE!')

while True:
    try:
        conversa = Conversa(driver)

        if not conversa.selecionar_conversa():
            print('Nenhuma conversa com notificação encontrada. Aguardando novas mensagens...')
            sleep(10)
            continue

        conversa.opcoes_mensagem()
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

        sleep(5)
