import time
import pyautogui

time.sleep(2)
print(pyautogui.position())

pyautogui.scroll(200)

import pandas as pd

tabela = pd.read_csv("produtos.csv", encoding='utf-8')
print(tabela)
