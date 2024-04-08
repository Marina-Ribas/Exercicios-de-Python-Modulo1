v = float(input('Qual a velocidade do carro?'))
if v>80:
    print(f'Sua velocidade é de {v} km/h, você foi multado!')
    m = float(v-80)*7
    print(f'Sua multa será de R${m:.2f} ')
else:
    print(f'Sua velocidade é de {v}, você não foi multado.')

