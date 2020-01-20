"""
Apenas uma criacao pessoal para treinos enquanto nao estou assistindo as aulas.
"""
controle = True
valor = 0
while controle:
    resposta = input("O que você deseja fazer?\n"
                     "1) Adicionar um valor a variavel valor\n"
                     "2) Verificar o valor da variavel valor\n"
                     "x) Sair do sistema ")
    if resposta == "1":
        quantidade = int(input("Quanto vc deseja adicionar? "))
        valor += quantidade
    elif resposta == "2":
        print(f'O valor atual da variavel eh de: {valor}')
    elif resposta == "x":
        controle = False
