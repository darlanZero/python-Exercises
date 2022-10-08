city = input('Digite o nome da cidade em que nasceu: ').strip()
s = city[:5].title() == 'Santo'
print(f'Existe a palavra Santo na cidade?\n'
      f'{s}.')