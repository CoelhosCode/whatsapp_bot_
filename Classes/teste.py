from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializar o WebDriver do Firefox
driver = webdriver.Firefox()

try:
    # Abrir o WhatsApp Web
    driver.get('https://web.whatsapp.com')

    # Aguardar manualmente até que você escaneie o QR Code (ou use uma abordagem automatizada)
    input("Pressione Enter após escanear o QR Code")

    # Testar o XPath do HEADER
    header_element = driver.find_element(By.XPATH, "//header")
    if header_element:
        print("HEADER encontrado.")

    # Testar o XPath do HEADER_PROFILE
    header_profile_element = driver.find_element(By.XPATH, "//header//div[contains(@class, 'x1n2onr6 x14yjl9h xudhj91 x18nykt9 xww2gxu')]")
    if header_profile_element:
        print("HEADER_PROFILE encontrado.")

    # Testar o XPath do HEADER_STATUS
    header_status_element = driver.find_element(By.XPATH, "//header//span/div[2]/div")
    if header_status_element:
        print("HEADER_STATUS encontrado.")

    # Testar o XPath do HEADER_NEW_CHAT
    header_new_chat_element = driver.find_element(By.XPATH, "//header//span/div[4]/div")
    if header_new_chat_element:
        print("HEADER_NEW_CHAT encontrado.")

    #Testar o XPath do Header_MENU_ARCHIVED
    header_menu_archived = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[3]/div/div[3]/button/div/div[2]')
    if header_menu_archived:
        #header_menu_archived.click()
        print('HEADER_MENU_ARCHIVED encontrado.')
        
        #Aguardar até achar o elemento de retornar
        #return_menu = WebDriverWait(driver, 10).until(
            #EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/div[2]/div[1]/span/div/span/div/header/div/div[1]/div/span'))
       # )

        #if return_menu:
            #return_menu.click()
            #print('Voltou ao meunu principal.')
        #else:
            #print('return_menu não encontrado.')

    # Testar o XPath do HEADER_MENU
    header_menu_element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/div[3]/header/div[2]/div/span/div[5]/div/span")
    if header_menu_element:
        header_menu_element.click()  # Clicar no elemento do menu
        print("Clicou no HEADER_MENU para abrir o pop-up.")

        # Aguardar até que o elemento do HEADER_MENU_POP_MENU esteja visível
        header_menu_pop_menu_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/div[3]/header/div[2]/div/span/div[5]/span/div/ul"))
        )

        if header_menu_pop_menu_element:
            print("HEADER_MENU_POP_MENU encontrado.")
        else:
            print("HEADER_MENU_POP_MENU não encontrado.")
    
    #Testar o XPATH do HEADER_MENU_CREATE_GROUP:
    header_menu_pop_menu_create_group_element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[3]/header/div[2]/div/span/div[5]/span/div/ul/li[1]/div')
    if header_menu_pop_menu_create_group_element:
        print('HEADER_MENU_POP_MENU_CREATE_GROUP encontrado.')

    #Testar o XPATH do HEADER_MENU_POP_MENU_CREATE_ROOM:
    header_menu_pop_menu_create_room_element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[3]/header/div[2]/div/span/div[5]/span/div/ul/li[2]/div')
    if header_menu_pop_menu_create_room_element:
        print('HEADER_MENU_POP_MENU_ROOM_CREATE encontrado.')

    #Testar o XPATH do HEADER_MENU_POP_MENU_STARRED:
    header_menu_pop_menu_starred_element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[3]/header/div[2]/div/span/div[5]/span/div/ul/li[4]')
    if header_menu_pop_menu_starred_element:
        print('HEADER_MENU_POP_MENU_STARRED encontrado.')

    #Testar o XPATH do HEADER_MENU_POP_MENU_SETTINGS:
    header_menu_pop_menu_settings_element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[3]/header/div[2]/div/span/div[5]/span/div/ul/li[6]')
    if header_menu_pop_menu_settings_element:
        print('HEADER_MENU_POP_MENU_SETTINGS encontrado.')
    
    #Testar o XPATH do HEADER_MENU_POP_MENU_LOGOUT:
    header_menu_pop_menu_logout_element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[3]/header/div[2]/div/span/div[5]/span/div/ul/li[7]')
    if header_menu_pop_menu_logout_element:
        print('HEADER_MENU_POP_MENU_LOGOUT_ELEMENT encontrado.')
    
    #Testar o XPATH do PANE:
    pane_element = driver.find_element(By.XPATH, '//*[@id="pane-side"]')
    if pane_element:
        print('PANE encontrado.')

    #Testar o XPATH do OPENED_CHATS:
    opened_chats_element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/div[3]/div/div[3]/div[2]')
    if opened_chats_element:
        print('OPENED_CHATS encontrado.')
    
    #Testar o XPATH do ICON:
    icon_element = driver.find_element(By.XPATH, "//*[contains(@class, '_ak8h')]")
    if icon_element:
        print('ICON encontrado.')

    #Testar o XPATH do NAME:
    name_element = driver.find_element(By.XPATH, "//*[contains(@class, '_ak8q')]")
    if name_element:
        print('NAME encontrado.')
    
    #Testar o XPATH do LAST_MESSAGE_TIME:
    last_message_time_element = driver.find_element(By.XPATH, "//*[contains(@class, '_ak8i')]")
    if last_message_time_element:
        print('LAST_MESSAGE_TIME encontrado.')
    
    #Testar o XPATH do LAST_MESSAGE:
    last_message_element = driver.find_element(By.XPATH, "//*[contains(@class, '_ak8k')]")
    if last_message_element:
        print('LAST_MESSAGE encontrado.')

    #Testar o XPATH do NOTIFICATION: 
    notification_element = driver.find_element(By.XPATH, "//*[contains(@class, '_ahlk')]")
    if notification_element:
        print('NOTIFICATION encontrado.')

finally:
    # Fechar o navegador
    driver.quit()
