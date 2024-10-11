'''
Passo 1 - Entrar no sitema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
Passo 2 - fazer login
Passo 3 - Importar base de dados
Passo 4 - cadastrar um produto
Passo 5 - Repetir o processo de cadastro até acabar os produtos
'''
import time
import pyautogui

# Passo 1 - Entrar no sitema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# pyautogui.write -> escrever um texto
# pyautogui.click -> clicar com o mouse
# pyautogui.press -> apertar uma tecla
# pyautogui.hotkey -> apertar uma atalho de teclado (Ctrl, C)

pyautogui.PAUSE = 0.5

# abrir o navegador
# apertar a tecla win
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Passo 2 - fazer login
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# dar uma pausa de 3 segundos
time.sleep(3)
pyautogui.press("tab")
pyautogui.write("teste@gmail.com")
pyautogui.press("tab")
pyautogui.write("afasfasffa")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)

# Passo 3 - Importar base de dados
import pandas as pd

tabela = pd.read_csv("C:/Users/igora/OneDrive/Documentos/GitHub/data_analysis_notebook/hashtag/produtos.csv", encoding='utf-8')
print(tabela)

# Passo 4 - cadastrar um produto
for linha in tabela.index:
    pyautogui.press("tab")
    # codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    # marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    # tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    # preco unitario
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    # obs
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")

# enviar 
pyautogui.press("enter")
# Passo 5 - Repetir o processo de cadastro até acabar os produtos


# time.sleep(5)
# print(pyautogui.position())

# pyautogui.scroll(200)