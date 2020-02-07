"""
Modulos Externos - Udemy

Utilizamos o gerenciador de pacotes Python chamado PIP - Python installer Package
Voce pode conhecer todos os pacotes externos oficiais em: https://pypi.org

colorama -> Utilizado para permitir impressao de texto colorido no terminal.
"""
from colorama import init, Fore, Back, Style
init()

print(Fore.RED + 'Some red Text')
print(Back.GREEN + "And with a Green Backgroud")
print(Style.DIM + "And in dim text")
print(Style.RESET_ALL)
print("Back to Normal")
