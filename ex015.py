day = int(input('Quantos dias seu carro foi alugado? '))
km = float(input('Quantos km rodados? '))
preCarro = (day * 60)
preKm = km * 0.15
preTotal = preCarro + preKm
print(f'Dias alugados: {day} dias;\n'
      f'Km rodados; {km} rodados;\n'
      f'Preço por diária: R${preCarro:.2f};\n'
      f'Preço por km rodado: R${preKm:.2f};\n'
      f'Preço total: R${preTotal:.2f}')
