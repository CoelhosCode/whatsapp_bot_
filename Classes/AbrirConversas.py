from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from Classes.ConfigNavegador import Navegador
from selenium.webdriver import ActionChains
import time
import emoji

class Conversa():
    # Xpath e Class_name utilizados para que o código funcione.
    NOTIFICACAO = "_ahlk"
    CONVERSAS = "//*[contains(@class, '_ak8l')]"
    CAIXA_DE_TEXTO_MENSAGEM = "_ak1q"

    def __init__(self, driver) -> None:
        self.driver = driver
        self.estados_conversas = {}
        self.mensagem_inicializada = True
    def selecionar_conversa(self):
        while True:
            time.sleep(3)
            try:
                # Verificação para achar notificações
                notificacoes = WebDriverWait(self.driver, 60).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME,Conversa.NOTIFICACAO))
                )
            except TimeoutException:
                print("Nenhuma notificação encontrada. Retentando...")
                continue
            
            # Leitura do nome do contato selecionado
            conversas = self.driver.find_elements(By.XPATH, Conversa.CONVERSAS)
            for conversa in conversas:
                try:
                    contato = conversa.find_element(By.CLASS_NAME,'_ak8q').text

                    # Se houver notificação, envia mensagem inicial
                    notificacao = conversa.find_element(By.CLASS_NAME, Conversa.NOTIFICACAO)
                    if int(notificacao.text) > 0:
                        conversa.click()
                        print(f"Conversa com {contato} selecionada.")
                    
                        if not self.estados_conversas.get(contato,  False):
                            self.enviar_mensagem_inicial()
                            self.estados_conversas[contato] = True
                        return True
                except Exception as e:
                    print(f"Erro ao processar conversa: {e}")
                    continue
    
    def enviar_mensagem(self, mensagem):
        try:
            # Tempo de espera para que a caixa de texto esteja visível.
            self.caixa_de_mensagem = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, Conversa.CAIXA_DE_TEXTO_MENSAGEM))
            )

            # Clica na caixa de texto para inserir a mensagem.
            self.caixa_de_mensagem.click()
            
            # Ação para escrever a mensagem
            acao_mouse = ActionChains(self.driver)
            acao_mouse.send_keys(mensagem).perform()
            print('Mensagem Escrita')

            # Envio da mensagem. Tempo de espera necessário para o bot não ser barrado pelo WhatsApp.
            time.sleep(2)
            acao = ActionChains(self.driver)
            acao.send_keys(Keys.ENTER).perform()
            print('Mensagem enviada')

        except TimeoutException:
            print('Elemento não encontrado!')

        except ValueError:
            print("Não foi possível converter o texto da notificação em um número.")
            return False

    #Função para enviar a mensagem inicial    
    def enviar_mensagem_inicial(self):
        remetente, texto_ultima_mensagem = self.ultima_mensagem()

        if remetente == 'cliente' and texto_ultima_mensagem in ['1', '2', '3', '4']:
            print('Continuando a conversa de acordo com o registro de mensagens.')
            return
        self.mensagem_inicial = (f"Olá, me chamo Beta, à assistente virtual da Rô.\nEssas são algumas opções disponíveis para interação comigo:\n1- {emoji.emojize(':etiqueta:')}Tabela de preços.\n2- {emoji.emojize(':relógio_temporizador:')}Agendamento de horários.\n3- {emoji.emojize(':telefone_celular:')}Falar diretamente com a Rô.\n4- {emoji.emojize(':coração_partido:')}Finalizar Atendimento."
        )
        self.enviar_mensagem(self.mensagem_inicial)

        mensagens_recebidas = self.driver.find_elements(By.CLASS_NAME, 'message-in')
        self.numero_mensagens_anteriores = len(mensagens_recebidas)
        self.mensagem_inicializada = True

    #Função para obter mensagens da pessoa e do bot e armazena-las em listas diferentes
    def obter_mensagens(self):
        mensagens_cliente = self.driver.find_elements(By.CLASS_NAME, 'message-in')
        mensagens_bot = self.driver.find_elements(By.CLASS_NAME, 'message-out')
        return mensagens_cliente, mensagens_bot
    
    def ultima_mensagem(self):
        mensagens_cliente, mensagens_bot = self.obter_mensagens()

        #Pegará a ultima mensagem
        ultima_mensagem_cliente = mensagens_cliente[-1] if mensagens_cliente else None
        ultima_mensagem_bot = mensagens_bot[-1] if mensagens_bot else None

        #Verificação pra saber de quem foi a ultima mensagem
        if ultima_mensagem_cliente and ultima_mensagem_bot:
            if ultima_mensagem_cliente.location['y'] > ultima_mensagem_bot.location['y']:
                texto = ultima_mensagem_cliente.find_element(By.CLASS_NAME, 'selectable-text').text
                return "cliente", texto
            else:
                texto = ultima_mensagem_bot.find_element(By.CLASS_NAME, 'selectable-text').text
                return "bot", texto
        elif ultima_mensagem_cliente:
            texto = ultima_mensagem_cliente.find_element(By.CLASS_NAME, 'selectable-text').text
            return "cliente", texto
        elif ultima_mensagem_bot:
            texto = ultima_mensagem_bot.find_element(By.CLASS_NAME, 'selectable-text').text
            return "bot", texto
        
        return None, None
    
    #Função para aguarda a resposta do cliente
    def aguardar_resposta(self, timeout = 10):
        tempo_inicial = time.time()
        while time.time() - tempo_inicial < timeout:
            remetente, texto = self.ultima_mensagem()
            if remetente == 'cliente':
                return texto
            time.sleep(5)
        print("Tempo excedido para resposta. Saindo da conversa.")
        self.sair_conversa()
        return None

    #Envio das opçoes disponíveis para interação com o bot
    def opcoes_mensagem(self):
        while True:
            texto = self.aguardar_resposta(timeout=10)
            if texto is None:
                break
            if texto == '1':
                self.enviar_mensagem('Segue a tabela de preços:')
            elif texto == '2':
                self.enviar_mensagem('Segue o link para agendamento de horários.')
            elif texto == '3':
                self.enviar_mensagem('Link para falar com a Rô: https://tinyurl.com/RobertaFrancaDesigner')
            elif texto == '4':
                self.enviar_mensagem(
                    f"Atendimento finalizado. Obrigado por confiar no trabalho da Rô! {emoji.emojize(':rosto_sorridente_com_3_corações:, :coração_vermelho:')} Nos vemos em breve."
                )
                self.sair_conversa()
                break
            else:
                self.enviar_mensagem("Desculpe, não entendi. Por favor, escolha uma opção válida.")


    def sair_conversa(self):
        self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.ESCAPE)
