n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
n3 = int(input('Digite o terceiro número:'))

lista = [n1, n2, n3]
lista.sort()
print(f'Os números digitados fora: {n1}, {n2} e {n3}')
print(f'O menor número digitado foi:{lista[0]}')
print(f'O maior número digitado foi:{lista[-1]}')
