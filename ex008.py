m = float(input('digite aqui quantos metros quer medir: '))
decim = m * 10
cm = m * 100
mm = m * 1000 or cm * 100
km = m / 1000
hm = m / 100
dm = m / 10
print(f'Sendo que você tem {m} metros, logo se tem {cm:.0f} centímetros, subsequentemente,'
      f'\nse tem {mm:.0f} milímetros. \nMas, não nos esqueceremos dos {decim:.0f} decímetros.')
print(f'Sendo que tu tem {m} metros, logo, se tem {km:.3f} km,\n {hm:.2f} hectômetros,\n e por fim,\n {dm:.1f} decâmetros.')
