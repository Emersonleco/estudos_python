print('Calcule a média de quatro notas')
n1 = float(input('Primera Nota:'))
n2 = float(input("Segunda Nota:"))
n3 = float(input('Terceira Nota:'))
n4 = float(input('Quarta Nota:'))
media = (n1 + n2 + n3 + n4) / 4
if 7 <= media < 10:
    print("APROVADO")
elif media < 7:
    print("REPROVADO")
else:
    print('APROVADO COM DISTINÇÃO')
