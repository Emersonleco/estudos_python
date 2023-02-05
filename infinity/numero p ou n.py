#print('Faça um Programa que peça ao usuário um valor e mostre na tela se o valor é positivo ou negativo.')
num = int(input('Digite um número: '))
if num>0:
    print(f'O número é {num} positivo')
elif num<0:
    print(f'O número {num} é negativo')
else:
    print(f'O número {num} é neutro')



