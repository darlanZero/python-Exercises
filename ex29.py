VelCarro = float(input('Qual é a velocidade do Carro em Km/h?' ))
LimiPermitido = int(80)
multa = int(7)
if VelCarro > LimiPermitido:
    preProc = (VelCarro - LimiPermitido)
    Mul = (multa * preProc)
    print(f'MULTADO! você ultrapassou o limite de velocidade permitido.\n'
          f'Sendo o limite de KM {LimiPermitido:.2f} e KM do carro {VelCarro:.2f}, \n'
          f'Você deve pagar uma multa de {Mul:.2f} reais baseada na sua KM restante de {preProc:.2f} KM.')
else:
    print(f'Você Passou na localidade sem ultrapassar o limite de velocidade. \n'
          f'Tenha um otimo dia! Dirija com segurança!')
