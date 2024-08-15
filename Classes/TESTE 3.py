from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

def iniciar_whatsapp():
    # Inicializa o WebDriver (substitua 'geckodriver' pelo caminho correto se necessário)
    driver = webdriver.Firefox()
    driver.maximize_window()

    # Abre o WhatsApp Web
    driver.get("https://web.whatsapp.com")

    # Aguarda que o usuário faça login (pode usar uma espera manual)
    input("Depois de escanear o código QR, pressione Enter para continuar...")

    try:
        conversa = driver.find_element(By.XPATH, "//*[contains(@class, '_ak8q')]")
        conversa.click()

        # XPath do elemento que você quer encontrar
        xpath_elemento = "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p"

        # Espera até que o elemento seja clicável
        caixa_de_texto = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, xpath_elemento))
        )
        sleep(2)
        # Clica no elemento
        caixa_de_texto.click()
        # Insere a mensagem
        actions = ActionChains(driver)
        actions.move_to_element(caixa_de_texto).click().perform()
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath_elemento))
        )
        caixa_de_texto.click()
        caixa_de_texto.send_keys("Olá, esta é uma mensagem enviada automaticamente pelo bot!")

    except TimeoutException:
        print("O elemento não foi encontrado ou não está clicável.")
    
    finally:
        # Você pode adicionar uma espera aqui para ver o resultado antes de fechar
        input("Pressione Enter para fechar o navegador...")
        driver.quit()

if __name__ == "__main__":
    iniciar_whatsapp()
