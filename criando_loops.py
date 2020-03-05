"""
criando a propria versao de um loop


"""
for num in [1, 2, 3, 4, 5]:
    print(num)

print()

for letra in 'Geek University':
    print(letra)


def meu_for(iteravel):
    it = iter(iteravel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


print()
meu_for([1, 2, 3, 4, 5, "oi"])
