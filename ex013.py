Sala = float(input('Salário Mensal do funcionário: '))
AuSala = Sala * 0.15
NovoSala = Sala + AuSala
print(f'tendo o funcionário o salário de {Sala};\n'
      f'E seu aumento salarial de {AuSala:.2f}, ao ter 15% de aumento,;\n'
      f'Seu novo salário será {NovoSala:.2f}. Parábens!')
