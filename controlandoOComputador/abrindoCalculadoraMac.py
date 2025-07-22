import pyautogui
import time

# Espera 2 segundos pra você sair do VSCode e deixar o Mac "livre"
time.sleep(2)

#move o mouse ate o botao de iniciar
pyautogui.moveTo(1322, 46)

# Atalho do Spotlight
pyautogui.hotkey('command', 'space')
time.sleep(2)  # Espera o Spotlight aparecer certinho

# Digita "Calculadora"
pyautogui.typewrite('Calculadora', interval=0.1)
time.sleep(1)

# Pressiona Enter pra abrir
#pyautogui.press('enter')

#pyautogui.typewrite('123+456')
#time.sleep(2)

pyautogui.press('enter')



