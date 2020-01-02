"""
Estruturas condicionais
if, else, elif


"""

idade = input("Digite a idade: ")
print(idade + " anos.")

if int(idade) < 18:
    print("Menor de idade!")
elif int(idade) == 18:
    print("Acabou de atingir a idade necessaria!")
else:
    print("Maior de idade!")