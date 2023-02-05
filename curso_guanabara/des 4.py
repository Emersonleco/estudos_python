algo = input('Digite algo:')
print(f'A informação {algo} é do tipo primitivo {type(algo)}')
print(f'É alfanumerico? {algo.isnumeric()}')
print(f'Só tem espaço?, {algo.isspace()}')
print(f'É alfabético?, {algo.isalpha()}')
print(f'É alfanumerico?,{algo.isalnum()}')
print(f'Está em minúsculas?, {algo.islower()}')
print(f'Está em maiúsculas?, {algo.isupper()}')
print(f'Está capitalizada?, {algo.istitle()}')



