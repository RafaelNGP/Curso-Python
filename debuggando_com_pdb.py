"""
PDB => Python Debbuger
Para utilizar o PDB, precisamos importar a biblioteca pdb e depois a funcao set_trace()
"""
# Usando a IDE

def dividir(a, b):
    try:
        return int(a) / int(b)
    except (NameError, ZeroDivisionError) as err1:
        print(f"Erro de valor. Erro: {err1}")


print(dividir(4, 7))


# Comandos basicos do PDB
# l (listar onde estamos no codigo)
# n (proxima linha)
# p (imprime variavel)
# c (continua a execucao - sai do debugging)
# pdb
nome = 'Rafael'
sobrenome = 'Ferreira'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programacao em Python: Essencial'
final = nome_completo + ' faz o curso: ' + curso
print(final)
