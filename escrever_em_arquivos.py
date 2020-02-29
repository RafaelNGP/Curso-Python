"""
Escrevendo em arquivos

Ao abrir um arquivo para leitura, nao podemos realizar a escrita nele, apenas ler.
Da mesma forma, se abrirmos um arquivo para escrita, nao podemos le-lo, somente escrever.
"""

# exemplo de escrita - modo 'w' - write(escrita)

with open('novo.txt', 'r+') as arquivo:
    while True:
        fruta = input("Informe uma fruta ou digite 'sair': ")
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            arquivo.seek(0)
            print(arquivo.read())
            break
