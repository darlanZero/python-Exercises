PreTo = float(input('Preço Inicial: '))
Des = 0.05
SubPre = PreTo * Des
FinPre = PreTo - SubPre
print(f'Preço Total: R${PreTo}\n'
      f'Desconto Obtido: 5%\n'
      f'Desconto Total: R${SubPre:.2f}\n'
      f'Preço Final: R${FinPre:.2f}')
