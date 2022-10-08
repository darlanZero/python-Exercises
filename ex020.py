import  random
al1 = input('Nome do 1° aluno: ')
al2 = input('Nome do 2° aluno: ')
al3 = input('Nome do 3° aluno: ')
al4 = input('Nome do 4° aluno: ')
List = [al1, al2, al3, al4]
random.shuffle(List)
print(f'Tendo em vista os alunos {al1, al2, al3, al4};\n'
      f'A ordem de apresentação do trabalho será {List}.')
