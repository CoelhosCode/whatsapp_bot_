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