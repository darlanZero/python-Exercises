num = input('Informe um número: ')
jun = '000' + num
tam = len(jun)
print('Leitor Númérico!'
      f'Analisando o número {num}...')
print(f'Unidade: {jun [tam - 1]}\n'
      f'Dezena: {jun [tam - 2]}\n'
      f'Centena: {jun [tam - 3]}\n'
      f'Milhar: {jun [tam - 4]}')

# Também pode-se fazer num = int(input('Informe um número: '))
# u = num // 1 % 10
# d = num // 10 % 10
# c = num // 100 % 10
# m = num // 1000 % 10
# print(f'Unidade: {u}\n'
# f'Dezena: {d}\n'
# f'Centena: {c}\n'
# f'Milhar: {m}')
