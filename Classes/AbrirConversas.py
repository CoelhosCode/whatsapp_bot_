from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from ConfigNavegador import Navegador
from selenium.webdriver import ActionChains
from time import sleep

class Conversa():
    # Xpath e Class_name utilizados para que o código funcione.
    NOTIFICACAO = "_ahlk"
    CONVERSAS = "//*[contains(@class, '_ak8l')]"
    CAIXA_DE_TEXTO_MENSAGEM = "_ak1l"

    def __init__(self, driver) -> None:
        self.driver = driver

    def selecionar_conversa(self):

        # Tempo de espera para que o elemento de NOTIFICACAO fique visível.
        self.notificacao_elemento = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, Conversa.NOTIFICACAO))
        )
        # Encontra todas as conversas dentro do WhatsApp.
        self.conversas = self.driver.find_elements(By.XPATH, Conversa.CONVERSAS)

        # Um loop para iteração com todas as conversas para verificar se há notificações.
        for conversas_com_notificacao in self.conversas:
            try:
                # Procura se há notificações na conversa atual.
                notificacao = conversas_com_notificacao.find_element(By.CLASS_NAME, Conversa.NOTIFICACAO)
                self.numero_notificacoes = int(notificacao.text)
            
                print(f"Notificaçôes: {self.numero_notificacoes}")
                
                # Clica na conversa se houver notificações.
                if self.numero_notificacoes > 0:
                    conversas_com_notificacao.click()
                    print('Conversa Selecionada.')
                    return True
            except ValueError:
                print('Não foi possível converter o texto da notificação para número!')
            except:
                # Continua para a próxima conversa se não tiver notificações na conversa atual.
                continue

        print('Não há notificações.')
        return False
    
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
            sleep(2)
            self.caixa_de_mensagem.send_keys(Keys.ENTER)
            print('Mensagem enviada')

        except TimeoutException:
            print('Elemento não encontrado!')

        except ValueError:
            print("Não foi possível converter o texto da notificação em um número.")
            return False
        
    def ler_mensagem(self):
        # Tempo de espera para que a pessoa responda o bot.
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, '_akbu'))
        )

        # Encontra a ultima mensagem.
        self.ultimas_mensagens = self.driver.find_element(By.CLASS_NAME, '_akbu')
        
        # Loop para iterar com a última mensagem e pegar seu texto.
        if self.ultimas_mensagens:
            self.ultima_mensagem = self.ultimas_mensagens[0]
            self.texto_ultima_mensagem = self.ultima_mensagem.find_element(By.CLASS_NAME, 'selectable-text').text
            return self.texto_ultima_mensagem