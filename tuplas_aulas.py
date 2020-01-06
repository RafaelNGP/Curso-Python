"""
Tuplas

Sao bastante parecidas com listas.
Existem basicamente duas diferencas:
    1- as tuplas sao representadas por ()
    2- as tuplas sao imutaveis. Ao se criar uma tupla, ela nao muda. Toda operacao em uma tupla gera uma nova tupla.
"""

tupla = 1, 2, 3, 4, 5, 6
print(tupla)
print(type(tupla))
# Podemos concluir que tuplas sao definidas por uso da virgula ',' e nao por parenteses ()

# Tuplas tbm podem ser geradas dinamicamente usando range
print()
tupla = tuple(range(11))
print(tupla)

# Desempacotamento de Tupla
print()
tupla = ("Geek University", "Programacao em Python", "Essencial")
escola, curso, nivel = tupla
print(f'Seja bem vindo a {escola}, ao curso de {curso} de nivel {nivel}!')

# Concatenacao de tuplas
print()
tupla1 = 1, 2, 3
tupla2 = 4, 5, 6
print(tupla1)
print(tupla2)
print(tupla1 + tupla2)
print(tupla1)
print(tupla2)
# Tuplas sao imutaveis
print()
# Verificar se determinado elemento esta contido na tupla
print(3 in tupla1)
#
print()
# Iterando sobre tuplas
for n in tupla1:
    print(n)

for indice, valor in enumerate(tupla1):
    print(indice, valor)
#
print()
# Contando elementos dentro de uma tupla
print(tupla1.count(1))

# Dicas na utilizacao de tuplas
# Usar tuplas sempre que nao for necessario modificar os dados contidos dentro de uma colecao:
# Ex1 - Nunca sera necessario adicionar um novo mes
meses = "Janeiro", "Fevereiro", "Marco", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
print(meses[0])
print(meses.index("Maio"))