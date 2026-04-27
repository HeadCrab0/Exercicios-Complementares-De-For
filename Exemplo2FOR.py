quant_alunos= int(input("Digte a quantidade de alunos: "))
quant_notas= int(input("Digte a quantidade de notas: "))

for a in range(quant_alunos):
    soma=0
    for n in range(quant_notas):
        nota = float(input("Informe uma nota: "))
        soma += nota
    media = soma / quant_notas
    print(f'media: {media:.2f}'
  
