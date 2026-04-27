
soma = 0

for cont in range(1, 1000):
    if cont % 3 == 0 or cont % 5 == 0:
        soma += cont
print(f'O valor da soma dos multiplos de 3 e 5 é: {soma}')
