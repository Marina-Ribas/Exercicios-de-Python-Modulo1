'''nome = input('Digite seu nome completo:')
print(nome)
print(nome.upper())
print(nome.lower())
print(len(nome.replace(' ', '')))
divido = (nome.split ())
print(len(divido [0]))'''


nome2 = input('Digite seu nome completo:')
print('Analisando seu nome...')
print(f'Seu nome em letras maiúsculas é: {nome2.upper()}')
print(f'Seu nome em letras minúsculas é: {nome2.lower()}')
print(f'Seu nome tem ao todo {len(nome2.replace(' ', ''))} letras.')
divido = (nome2.split())
print(f'Seu primeiro nome é {divido[0]} e ele tem {len(divido[0])} letras')
print(f'Seu último nome é {divido[-1]} e ele tem {len(divido[-1])} letras')
