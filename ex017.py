import math

a = float(input('Adicione aqui seu cateto oposto: '))
b = float(input('Em seguida, adicione seu cateto adjacente: '))
c = math.hypot(a, b)
# c = (a ** 2 + b  ** 2) ** (1/2)
print(f'Sendo seu cateto oposto {a} e\n'
      f'Seu cateto adjacente {b},\n'
      f'Logo, sua hipotenusa seria {c:.2f}.')
