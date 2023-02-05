#Numeros a digitar
num1 = float(input('Digite um número:'))
num2 = float(input('Digite outro:'))
#Escolha de operação
print('Qual operação você quer realizar?')
print('1. Adição')
print('2. Subtração')
print('3. Multiplicação')
print('4. Divisão')
op: int = int(input('Qual operação a ser realizada:'))
#Escolhendo as operações
if op == 1:
    resultado = num1+num2
elif op == 2 :
    resultado = num1-num2
elif op == 3 :
    resultado = num1*num2
elif op == 4 :
    resultado = num1 / num2
else:
    print('Operação inválida.')
    quit()

#Clasificar par e impar
if resultado % 2 == 0:
    par_impar = 'par'
else:
    par_impar = 'ímpar'
#Positivo e negativo
if resultado >= 0:
    pos_neg = "positivo"
else:
    pos_neg = 'negativo'
#interiro ou  decimal
if resultado.is_integer():
    int_dec = 'inteiro'
else:
    int_dec = 'decimal'
#RESPOSTA
print(f'Resultado: {resultado}')
print(f'O resultado da operação é um número {par_impar}, {pos_neg} e {int_dec}')
