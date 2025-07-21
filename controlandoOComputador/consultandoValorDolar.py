import pyautogui as posicaoMouse
import pyautogui as tempoEspera

#Tempo de espera para que o computador possa pensar
tempoEspera.sleep(2)

#Movendo o mouse até o botão iniciar
posicaoMouse.moveTo(36, 1056)

#Tempo de espera para que o computador possa pensar
tempoEspera.sleep(2)

#Clicando na posição
posicaoMouse.click(36, 1056)

#Tempo de espera para que o computador possa pensar
tempoEspera.sleep(2)

#Digitando o nome do navegador 
posicaoMouse.typewrite('Google Chrome')

#Tempo de espera para que o computador possa pensar
tempoEspera.sleep(3)

#Precionando a tecla enter
posicaoMouse.press('enter')

#Digitando a palavra Dólar para pesquisar
posicaoMouse.typewrite('Dolar Hoje')

#Tempo de espera para que o computador possa pensar
tempoEspera.sleep(3)

#Apertando a tecla enter para pesquisar o dolar
posicaoMouse.press('enter')