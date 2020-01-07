"""
Conjuntos

- Em qualquer linguagem: estamos fazendo referencia a Teoria dos conjuntos da Matematica.
- Em Python os conjuntos sao chamados de Sets

Dito isto, da mesma forma que na matematica:
    - sets (conjuntos) nao possuem valores duplicados
    - sets (conjuntos) nao possuem valores ordenados
    - elementos nao sao acessados via indice, ou seja, conjuntos nao sao indexados

Conjuntos sao bons para se utilizar quando precisamos armazenar elementos, mas nao nos importamos com
a ordenacao deles. Quando nao precisamos nos preocupar com chaves, valores e itens duplicados.

Os conjuntos (sets) sao referenciados em Python com chaves {}

Diferenca entre sets e mapas (dicionarios) em Python:
    -Um dicionario tem chave/valor
    -Um conjunto tem apenas valor
"""
# Definindo um conjunto
# Forma 1
# Repare que temos valores repetidos e ele nao adiciona elas.
S = set({1, 2, 3, 4, 5, 6, 7, 2, 3})
print(S)
print(type(S))

# Forma 2
S = {1, 2, 3, 4, 6, 7, 5, 5, 5}
print(S)
print(type(S))

# Verificando conteudo
if 3 in S:
    print("Tem")
else:
    print("N tem")

print()
# Importante lembrar que alem de nao termos valores duplicados, nao temos ordem.
dados = 99, 75, 4, 356, 74, 377, 4, 356
lista = list(dados)
tupla = tuple(dados)
dicionario = {}.fromkeys(dados, "dict")
s = {99, 75, 4, 356, 74, 377, 4, 356}
print(f'lista: {lista} com {len(lista)} elementos.\n'
      f'tupla: {tupla} com {len(tupla)} elementos.\n'
      f'dicionario: {dicionario} com {len(dicionario)} elementos.\n'
      f'set: {s} com {len(s)} elementos.')

# Tambem eh possivel misturar os tipos de elementos no set
S = {'s', 2, 1.90, True}
print(S)
# Podemos iterar tambem
for valor in S:
    print(valor)
    print(type(valor))
# Usos interessantes com sets
print("Usando cast para filtrar os valores repetidos.")
print(len(set(s)))

# Adicionando elementos
S.add(4)
print(S)

# Removendo elementos
# Forma 1 - Pode gerar keyError.
S.remove(4)
print(S)

# Forma 2
S.discard(2)
print(S)

# Copiando um conjunto para outro.
# Forma 1 - Deep Copy
s = S.copy()
print(s)
print(S)
print()

# Forma 2 - Shallow Copy
S = {2, True, 124, "true"}
s = S
print(s)
print(S)
s.add(555)
print(S)
print(s)
# limpando tudo #
s.clear()
S.clear()
print()
##########################################
# Imagine que temos dois conjuntos:#######
# Conjunto de estudantes: Python e Java###
##########################################
# Perceba que temos alunos iguais em ambos os cursos.
estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Forma 1 - Utilizando Union
estudantes_cursos = estudantes_python.union(estudantes_java)
print(estudantes_cursos)

# Forma 2 - Utilizando o caractere |
estudantes_cursos = estudantes_python | estudantes_java
print(estudantes_cursos)

# Gerar um conjunto de estudantes que estao em ambos os cursos
# Forma 1 - Utilizando intersection
estudantes_cursos = estudantes_java.intersection(estudantes_python)
print(estudantes_cursos)

# Forma 2 - Utilizando o caractere &
estudantes_cursos = estudantes_java & estudantes_python
print(estudantes_cursos)

# Gerar um conjunto de estudantes que nao estao no outro
so_python = estudantes_python.difference(estudantes_java)
so_java = estudantes_java.difference(estudantes_python)
print(so_python)
print(so_java)

# Sum, max, min, len.
s = {1, 2, 3, 4, 5, 6, 100}
print(sum(s))
print(max(s))
print(min(s))
print(len(s))
