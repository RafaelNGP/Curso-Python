def voltar_linhas(n):
    arquivo.seek(n)


arquivo = open("texto.txt", 'r')
# print(arquivo.read())
print(len(arquivo.read()))

# este read nao executa por ter ido com o cursor ate o final para fazer a conta acima
print(arquivo.read())
# Usando o seek, ele volta o cursos para onde mandar (indice 5)
voltar_linhas(5)
print(arquivo.read())
voltar_linhas(0)
print(arquivo.read(50))
print(arquivo.read(50))
voltar_linhas(0)
print()

ret = arquivo.readline()
print(type(ret))
print(ret)
print(ret.split(' '))

voltar_linhas(0)
print(len(arquivo.readlines()))
print(arquivo.closed)

arquivo.close()
print(arquivo.closed)
