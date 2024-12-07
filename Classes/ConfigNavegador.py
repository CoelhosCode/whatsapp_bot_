from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import os
class Navegador():
    def __init__(self) -> None:
        pass
    
    def configuracao_navegador(self):
        # Camiho do perfil do Firefox
        perfil_usuario = FirefoxProfile(os.getenv("CAMINHO_PERFIL_FIREFOX"))
        #Configuração do Firefox para usar o perfil
        opcoes = Options()
        opcoes.set_preference("javascrpit.enable", False)
        opcoes.profile = perfil_usuario
        #Inicia o Driver do Firefox
        self.driver_navegador = webdriver.Firefox(options=opcoes)
        #Maximiza a tela do navegador
        self.driver_navegador.maximize_window()
        # Entra no site do WhatsApp.
        self.driver_navegador.get('https://web.whatsapp.com')

        return self.driver_navegador

    def fechar_navegador(self):
        # Função para fechar o navegador.
        if self.driver_navegador:
            self.driver_navegador.quit()
            