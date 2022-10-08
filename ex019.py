import random
al1 = input('Escreva aqui o nome do seu primeiro aluno: ')
al2 = input('Escreva aqui o nome do segundo aluno: ')
al3 = input('Escreva aqui o nome do terceiro aluno: ')
al4 = input('Escreva aqui o nome do quarto aluno: ')
alunos = [al1, al2, al3, al4]
esco = random.choice(alunos)
print(f'Tendo os Alunos {al1}, {al2}, {al3}, e {al4} como base para apagar o quadro,\n'
      f'Você escolheu o aluno: {esco}.')