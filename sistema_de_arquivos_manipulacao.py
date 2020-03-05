"""
Sistema de Arquivos - Manipulacao

"""
import os
import tempfile

# verificando se arquivo existe
print(os.path.exists('texto.txt'))

# verificando se pasta existe
print(os.path.exists('geek'))

# verificando se o arquivo existe dentro da pasta
print(os.path.exists('geek/university/geek3.py'))


# Nao funcionando no windows por algum motivo
# os.mknod('arquivo-teste.txt')
# os.mknod('\\geek\\university.txt')

# comentado pra nao gerar erro
# os.makedirs('templates\\geek\\university\\outro')

# os.rename('templates', 'geekTemplates')

# # Criando uma pasta temporaria com um arquivo normal dentro
# with tempfile.TemporaryDirectory() as tmp:
#     print(f"Criei o diretorio temporario em {tmp}")
#     with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
#         arquivo.write("Geek University\n")
#     input()

# Criando um arquivo temporario
with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Isto eh um teste')
    tmp.seek(0)
    print(tmp.read())
