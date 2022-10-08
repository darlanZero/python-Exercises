import random
from time import sleep

print('-=-' * 19)
print('Vou pensar em um número entre 0 e 5, adivinhe se puder!')
print('-=-' * 19)
PenUm = int(input('Em que número estou pensando? '))
num = 0, 1, 2, 3, 4, 5
numEscolhido = random.choice(num)
# também se usa randint
print('PROCESSANDO...')
sleep(2)
if PenUm == numEscolhido:
    print(f'Parábéns, você passou!')
else:
    print(f'Não foi dessa vez, tente novamente!')
print(f'O número escolhido pela máquina é {numEscolhido}\n'
      f'O número escolhido pelo Jogador foi {PenUm}')
