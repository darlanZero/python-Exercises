nome = str(input('digite seu nome completo: '))
# pode-se usar .strip() na string
up = nome.upper()
low = nome.lower()
esp = (nome.count(" "))
co = len(nome)
pr = nome.split()[0]
# 0 também justifica que quero saber seu primeiro caractere em uma lista 'split'.
# Também pode usar nome.find(' ')
PrCo = len(pr)
print('Análisador de Nomes!\n'
      f'Sendo seu nome {nome}, logo,\n'
      f'Seu nome em maiúsculas é {up}\n'
      f'Seu nome em minúsculas é {low}\n'
      f'E seu nome tem {co - esp} letras.\n'
      f'Por fim, seu primeiro nome é {pr} e tem {PrCo} letras.')
