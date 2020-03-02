"""
StringIO - Utilizado para ler e criar arquivos em memoria

Para ler ou escrever dados em arquivos do sistema operacional, o sofware precisa ter permissao:
    - permissao de leitura para ler o arquivo
    - permissao de escrita para escrever no arquivo

Podemos criar um arquivo em memoria ja com uma string na memoria ou ate mesmo
vazio para inserir texto depois.
"""
from io import StringIO
mensagem = 'esta eh apenas uma string comum.'
arquivo = StringIO(mensagem)
arquivo.write("String de teste")
arquivo.write("Vejamos que tipo de escrita vai rolar aqui")
arquivo.seek(0)
print(arquivo.read())
