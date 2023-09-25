#Esse script tem como objetivo inicializar o navegador desejado (nesse caso o Google Chrome), acessar um site específico e fazer login em seu usuário.
#Foi projetado inicialmente para acessar de maneira automática um sistema de monitoramento de temperatura, tensão e sinal de uma estação de rádio.
#Necessária a instalação do ambiente Python, webdriver do navegador escolhido além da biblioteca Selenium que atua na automação Web.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Inicializa o driver do Chrome
driver = webdriver.Chrome()

# Abre o site
driver.get("endereço do site desejado")

# Realiza o login (ajuste os seletores conforme o site)
usuario_elem = driver.find_element_by_name("username")
usuario_elem.clear()
usuario_elem.send_keys("admin")

senha_elem = driver.find_element_by_name("password")
senha_elem.clear()
senha_elem.send_keys("admin")
senha_elem.send_keys(Keys.RETURN)
