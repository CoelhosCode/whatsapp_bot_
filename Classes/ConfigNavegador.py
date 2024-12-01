from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

class Navegador():
    def __init__(self) -> None:
        pass
    
    def configuracao_navegador(self):
        #Inicia o Driver do Firefox
        self.driver_navegador = webdriver.Firefox()
        #Maximiza a tela do navegador
        self.driver_navegador.maximize_window()
        # Entra no site do WhatsApp.
        self.driver_navegador.get('https://web.whatsapp.com')

        return self.driver_navegador

    def fechar_navegador(self):
        # Função para fechar o navegador.
        if self.driver_navegador:
            self.driver_navegador.quit()
            