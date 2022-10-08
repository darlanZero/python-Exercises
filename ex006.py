var = int(input('Digite aqui seu número: '))
do = var * 2
tri = var * 3
ra = var ** (1 / 2)
# também se usa pow(var, (1/2)
print(
    f'logo, seu número é {var}, o dobro dele é {do},\n o triplo dele é {tri}, e, por fim, \n sua raíz quadrada é '
    f'{ra:.2f}.')
