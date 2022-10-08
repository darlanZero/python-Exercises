name: str = (input('Qual o seu nome completo? ').strip()).title()
fi = 'Silva' in name
print(f'Diga se seu sobrenome é "Silva"!\n'
      f'Seu nome tem Silva nele?\n '
      f'{fi}.')

# nome = str(input('Insira o seu nome completo: ')).title().strip()
# divideNome = nome.split()
# print(f'Seu nome é {nome}',
# f'Há Silva em seu nome? {"Silva" in divideNome[0:]}\n',)
