r1 = float(input('Digite o comprimento da primeira reta:'))
r2 = float(input('Digite o comprimento da segunda reta:'))
r3 = float(input('Digite o comprimento da terceira reta:'))
lista = [r1, r2, r3]
lista.sort()
soma = (lista[0]+lista[1])
if soma>lista[2]:
    print('As retas informadas pode formar um triangulo!')
else:
    print('As retas informadas não podem formar um triangulo!')

#A soma das medidas dos dois menores tem que ser maior que a medida do terceiro