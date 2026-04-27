salInicial = 2000
anoInicial = 2015

while anoInicial != 2026:
    salInicial = salInicial + (salInicial*0.015)
    anoInicial +=1

print(f'O salário do funcionário em 2026 será: {salInicial:.2f}')