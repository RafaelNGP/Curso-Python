"""
Em Python um valor eh considerado do tipo String sempre que estiver entre aspas (simples e duplas)
"""
nome = "Rafael \nThunderstorm"
print(nome.upper())
print(nome.split())

nome = "geek university".title()
print(nome)
print(nome.lower())

# Slice/fatia de Strings
print(nome[0:4])
print(nome[5:15])

print(nome.split()[0])
print(nome.split()[1])

# Do primeiro ao ultimo, invertido
print(nome[::-1])

print(nome.replace("G", "M"))

# Tipo de nome
print(type(nome))
