# PACKAGES
import pyautogui
import time
import pandas

#test
#test2

pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# PASSO 1: ENTRAR NO SITE
# abrir navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
#fazer uma pausa maior pq é no browser e depende de conexão a internet, então esperar um pouco a mais
time.sleep(3)

# PASSO 2: FAZER LOGIN
# clicar na caixa de e-mail
pyautogui.hotkey("win","up")
pyautogui.click(x=696, y=412)
pyautogui.write("othonluiz_othonluiz@hotmail.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("enter")
#fazer uma pausa maior pq é no browser e depende de conexão a internet, então esperar um pouco a mais
time.sleep(3)

# PASSO 3: ABRIR A BASE DE DADOS
#importando base de dados
tabela = pandas.read_csv("produtos.csv")
print(tabela)
for linha in tabela.index: #usou o index pois estamos lendo de linha em linha, se fosse coluna, trocaria o index por column por exermplo
  # PASSO 4: CADASTRAR 1 PRODUTO
  pyautogui.click(x=699, y=290)
  
  #codigo
  codigo = str(tabela.loc[linha, "codigo"])
  pyautogui.write(codigo)
  pyautogui.press("tab")
  #marca
  marca = str(tabela.loc[linha, "marca"])
  pyautogui.write(marca)
  pyautogui.press("tab")
  #tipo
  tipo = str(tabela.loc[linha, "tipo"])
  pyautogui.write(tipo)
  pyautogui.press("tab")
  #categoria
  categoria = str(tabela.loc[linha, "categoria"])
  pyautogui.write(categoria)
  pyautogui.press("tab")
  #preco
  preco = str(tabela.loc[linha, "preco_unitario"])
  pyautogui.write(preco)
  pyautogui.press("tab")
  #custo
  custo = str(tabela.loc[linha, "custo"])
  pyautogui.write(custo)
  pyautogui.press("tab")
  #obs
  obs = str(tabela.loc[linha, "obs"])
  if obs != "nan":
    pyautogui.write(obs)
  pyautogui.press("tab") #passa para o botão enviar
  
  #clicar no enviar
  pyautogui.press("enter")
  #voltar para o inicio da tela
  pyautogui.scroll(5000)
  

# PASSO 5: REPETIR PASSO 4 ATÉ ACABAR LISTA DE PRODUTOS

