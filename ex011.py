Alt = float(input('Qual a altura da parede?  '))
Lar = float(input('Qual a largura da parede? '))
Ar = Alt * Lar
QuantTinta = float(Ar / 2)
print(f'Sendo que a parede mede {Alt} M por {Lar} M;\n'
      f'A parede tem uma área total de {Ar} M².;'
      f'E para pintá-la toda, são necessários {QuantTinta} litros de tinta.')
