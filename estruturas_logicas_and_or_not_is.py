"""
Estruturas logicas: and (e), or (ou), not (nao), is (eh)

operadores unarios:
    -not

operadores binarios:
    -and or is

Regras:
Para o `and`, ambos os valores precisam ser True.
Para o `or`, um ou outro precisa ser True.
Para o `not`, o valor do booleano eh invertido.

"""
# Recolhendo os dados
ativo = input("Ativo? (s/n) ").title()
logado = input("Logado? (s/n) ").title()

# Convertendo em Booleano
if ativo == "S":
    ativo = True
else:
    ativo = False

# Convertendo em Booleano
if logado == "S":
    logado = True
else:
    logado = False

# Checando valores booleanos
if ativo and logado:
    print("\nSeja bem vindo!\n")
else:
    print("\nVoce precisa ativar sua conta. Por favor, cheque seu email.\n")

# Imprimindo os valores
print(ativo)
print(type(ativo))
print(logado)
print(type(logado))
