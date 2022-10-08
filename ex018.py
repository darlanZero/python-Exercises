from math import radians, sin, cos, tan
an = float(input('escreva aqui seu Ângulo: '))
sen = sin(radians(an))
cos = cos(radians(an))
tan = tan(radians(an))
print(f'o Ângulo {an} tem o seu seno de: {sen:.2f}.'
      f'\nLogo, seu cosseno é {cos:.2f};'
      f'\nE ao final, sua tangente é {tan:.2f}.')