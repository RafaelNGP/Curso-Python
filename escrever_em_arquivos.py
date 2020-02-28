"""
Escrevendo em arquivos

Ao abrir um arquivo para leitura, nao podemos realizar a escrita nele, apenas ler.
Da mesma forma, se abrirmos um arquivo para escrita, nao podemos le-lo, somente escrever.
"""

# exemplo de escrita - modo 'w' - write(escrita)

with open('novo.txt', 'w') as arquivo:
    while True:
        fruta = input("Informe uma fruta ou digite 'sair': ")
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break
