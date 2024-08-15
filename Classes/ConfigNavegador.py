from selenium import webdriver

class Navegador():
    def __init__(self) -> None:
        pass
    
    def configuracao_navegador(self):
        # Inicia o driver do Firefox.
        self.driver_navegador = webdriver.Firefox()
        # Maximiza a tela do navegador para não ocorrer cliques indesejados em lugares fora da tela do driver.
        self.driver_navegador.maximize_window()
        # Entra no site do WhatsApp.
        self.driver_navegador.get('https://web.whatsapp.com')
        return self.driver_navegador

    def fechar_navegador(self):
        # Função para fechar o navegador.
        if self.driver_navegador:
            self.driver_navegador.quit()
            