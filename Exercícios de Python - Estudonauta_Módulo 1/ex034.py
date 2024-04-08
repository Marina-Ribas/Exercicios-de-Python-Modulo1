s = float(input('Digite o seu salário:'))
a1 = s+s*(10/100)
a2 = s+s*(15/100)
if s>1250.00:
    print(f'Seu salário atual é de R${s:.2f}. Com o aumento seu novo salário será R${a1:.2f}')
else:
    print(f'Seu salário atual é de R${s:.2f}. Com o aumento seu novo salário será R${a2:.2f}')
