import pyautogui as posicaoAbreArquivos
import time
import subprocess

# Aguarda um tempo para o computador processar informações
time.sleep(2)

# Abre o TextEdit diretamente usando subprocess
subprocess.Popen(["open", "-a", "TextEdit"])

# Aguarda o TextEdit abrir
time.sleep(4)

# Escreve no TextEdit
posicaoAbreArquivos.typewrite("Abri o TextEdit com o Python")
time.sleep(4)

# Fecha a janela ativa
janelaAtiva = posicaoAbreArquivos.getActiveWindow()
time.sleep(2)
janelaAtiva.close()

# Aguarda e navega até botão 'Não Salvar' (podem variar as posições, depende da localização do botão)
time.sleep(2)
posicaoAbreArquivos.press('tab')  # Pode ser necessário pressionar tab mais de uma vez
time.sleep(1)
posicaoAbreArquivos.press('enter')  # Confirma para fechar sem salvar

print("Automação executada com sucesso no macOS!")
