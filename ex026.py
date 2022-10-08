fr: str = input('Digite uma frase:').lstrip().lower().replace('á', 'a').replace('ã', 'a').replace('â', 'a')
fo = fr.find('a') + 1
fu = fr.rfind('a') + 1
fa = fr.count('a')
input(f'A letra A aparece {fa} vezes na frase\n'
      f'A letra aparece pela primeira vez na posição {fo}.\n'
      f'A letra A aparece pela última vez na posição {fu}.')
