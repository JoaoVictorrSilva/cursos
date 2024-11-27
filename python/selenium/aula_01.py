import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

print('\n\n** Configurações de Servidor de Login **\n')

servidor_input = int(input('\nDigite o número do servidor: '))

while servidor_input != 1 and servidor_input != 2:
    print(f'\nServidor Inválido!')
    servidor_input = int(input(f'\nDigite 0 para sair ou digite novamente o número do Servidor: '))
    
    if servidor_input == 0:
        break

if servidor_input == 0:
    exit

if servidor_input == 1:
    url = 'http://44.239.145.169/login'
elif servidor_input == 2:
    url = 'http://34.212.126.243/login'

user = input('Digite o tenant do cliente: ')
user = 'conversao.' + user

browser = Chrome()
browser.get(url)

campo_usuario = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "usuario"))
)
campo_usuario.send_keys(user)

key = 'C0r1ng@$'
campo_senha = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.NAME, "senha"))
)
campo_senha.send_keys(key)

entrar = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.ID, "botao_submit"))
)
entrar.click()
time.sleep(3)

prosseguir = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.ID, "botao_prosseguir_informa_local_trabalho"))
)
prosseguir.click()
time.sleep(3)

configuracoes_link = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/menu/configuracao')]"))
)
configuracoes_link.click()
time.sleep(3)

programas_gerais = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.ID, "programas_gerais"))
)
programas_gerais.click()
time.sleep(3)

browser.quit()