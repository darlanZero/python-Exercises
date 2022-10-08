nam: str = input('Digite seu nome completo:').lstrip().title()
FirNam = nam.split()[0]
LaNam = nam.split()[-1]
print(f'Analisador de Nomes\n'
      f'Sendo seu nome completo {nam},\n'
      f'Logo, seu primeiro nome é {FirNam}\n'
      f'E seu último nome é {LaNam}.')
