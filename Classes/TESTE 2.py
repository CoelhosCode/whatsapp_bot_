from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from ConfigNavegador import Navegador
import time

# Iniciar o navegador.
driver = webdriver.Firefox()
driver.maximize_window()
driver.get('https://web.whatsapp.com')
print('Navegou até a página do WhatsApp Web')

# Aguardar o QR Code ser escaneado e esperar que a página carregue totalmente.
input('Pressione enter após escanear o QR Code')
print('QR Code escaneado!')


#try:
#    # Navegar para a página desejada
#    driver.get('https://web.whatsapp.com')
#    print("Navegou para a página do WhatsApp Web")
#
#
#    # Aguarde um tempo para a página carregar completamente (ajuste conforme necessário)
#    input("Pressione Enter após escanear o QR Code")
#    print("QR Code escaneado, continuação do script")
#
#    # Localizar o elemento onde o mouse deve passar
#    elemento_mouse = driver.find_element(By.XPATH, "//*[@id='main']/div[3]/div/div[2]/div[3]//div/div/div[1]/div[1]/div[1]/div")
#    print("Elemento para passar o mouse encontrado")
#
#    # Rolar a página para o elemento
#    driver.execute_script("arguments[0].scrollIntoView();", elemento_mouse)
#    print("Rolou para o elemento")
#
#    # Criar uma ação de movimento do mouse
#    action = ActionChains(driver)
#    action.move_to_element(elemento_mouse).perform()
#    print("Movimentou o mouse para o elemento")
#
#    # Aguarde um tempo para que o elemento oculto se torne visível (ajuste conforme necessário)
#    time.sleep(10)
#    print("Aguardou 10 segundos para o elemento oculto se tornar visível")
#
#    # Após passar o mouse, localizar o elemento oculto
#    elemento_oculto = driver.find_element(By.XPATH, "//*[@id='main']/div[3]/div/div[2]/div[3]//span[2]/div/div")
#    print("Elemento oculto encontrado")
#
#    # Clicar no elemento oculto
#    elemento_oculto.click()
#    print("Clicou no elemento oculto")
#
#    # Aguardar 30 segundos antes de fechar o navegador
#    time.sleep(30)
#    print("Aguardou 30 segundos")
#
#except Exception as e:
#    print(f"Erro: {e}")
#
#finally:
#    # Fechar o navegador
#    driver.quit()
#    print("Navegador fechado")
