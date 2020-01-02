"""
Como receber dados
Dados recebidos por Input sao reconhecidos como String, entao tem que fazer um cast para fazer contas com ela.

tipo(variavel)  --  int(vitimas)
"""

# entrada de dados
nome = input("Qual seu nome? ")
vitimas = int(input("Quantos inimigos derrubou hoje? "))

# Versao antiga
# saida de dados
# print('Seja bem vindo@ %s' % nome.lower().title())
# print("Incrivel %s! Voce esta dizendo que %s cairam hoje em campo de batalha perante sua supremacia?" % (nome, vitimas))

# versao mais atual
print(f'Seja bem vindo, {nome}!'.lower().title())
print(f'Incrivel {nome}! Voce esta dizendo que {vitimas} cairam hoje em campo de batalha perante sua supremacia?')