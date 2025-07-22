import pyautogui as escolha_opcao
import subprocess
import time

# Janela de seleção
opcao = escolha_opcao.confirm('Clique no botão desejado',
            buttons=['Excel', 'Word', 'TextEdit'])

if opcao == "Excel":
    # Abre o Excel (caso esteja instalado e reconhecido)
    subprocess.Popen(["open", "-a", "Microsoft Excel"])
    time.sleep(5)

    # Digita no Excel (janela precisa estar ativa)
    escolha_opcao.typewrite('Escolhi abrir o Excel')
    print("Você escolheu abrir o Excel")

elif opcao == "Word":
    # Abre o Word
    subprocess.Popen(["open", "-a", "Microsoft Word"])
    time.sleep(5)

    escolha_opcao.typewrite('Escolhi abrir o Word')
    print("Você escolheu abrir o Word")

else:
    # Abre o TextEdit (equivalente ao Notepad no macOS)
    subprocess.Popen(["open", "-a", "TextEdit"])
    time.sleep(5)

    escolha_opcao.typewrite('Escolhi abrir o TextEdit')
    print("Você escolheu abrir o Bloco de notas (TextEdit)")
