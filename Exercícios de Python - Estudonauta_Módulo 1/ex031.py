d = float(input('Qual a distância de sua viagem em Km?'))
p1 = float(d*0.50)
p2 = float(d*0.45)
if d<=200 :
    print(f'\033[34mSua viagem tem {d} Km e seu valor será R${p1:.2f}')
else:
    print(f'\033[35mSua viagem tem {d} Km e seu valor será R${p2:.2f}')
