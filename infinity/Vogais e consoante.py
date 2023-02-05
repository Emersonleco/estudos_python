# print ('faça um programa que verifique se a letra digtada é vogal ou consoante')
letra = input('Digite uma letra:')
if letra.lower() in "aeiou":
    print(f'A letra{letra} é uma vogal')
else:
    print(f'A letra {letra} é uma consoante')
