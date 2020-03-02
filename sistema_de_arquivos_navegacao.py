"""
Sistema de Arquivos e Navegacao

Para fazer uso da manipulacao de arquivos do sistema operacional, precisamos importar o
modulo os.

os -> Sistema Operacional.
"""
import os
import platform

# Printando o diretorio atual da aplicacao
print(os.getcwd())
# movendo um diretorio acima na hierarquia.
os.chdir("..")

# repetindo o processo
print(os.getcwd())
os.chdir("..")

print(os.getcwd())
os.chdir("..")

# podemos checar se um diretorio eh absoluto ou relativo
# Absoluto:
print(os.path.isabs('B:\\Desenvolvimento\\GruppeUdemy'))

# Relativo:
print(os.path.isabs('Desenvolvimento\\GruppeUdemy'))

# identificando o tipo de sistema operacional:
# posix = linux e mac
# nt = windows
print(os.name)
print(platform.uname())

# Entrando em outros niveis de diretorios.
print()
os.chdir('.\\Desenvolvimento\\GuppeUdemy')
print(os.getcwd())
# os.mkdir('geek2') comentado pq a pasta ja existe
# os.chdir(os.path.join(os.getcwd(), "geek2"))
# print(os.getcwd())

scanner = os.scandir()
arquivo = list(scanner)

print(os.listdir(os.getcwd()))
print(os.scandir(os.getcwd()))
print(arquivo)
print()
print(arquivo[0])
print(arquivo[0].name)
print(arquivo[0].is_file())
print(arquivo[0].is_dir())
print(arquivo[0].is_symlink())
print(arquivo[0].path)
print(arquivo[0].inode())
print(arquivo[0].stat())

# Quando usamos a opcao scandir, precisamos fecha-la
scanner.close()
