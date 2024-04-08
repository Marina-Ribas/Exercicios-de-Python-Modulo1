import random
from time import sleep
n = random.randint(0, 5)
print('-=-'*40)
tent = int(input('Descubra qual o número de 0 a 5:'))
print('-=-'*40)
print(f'Sua resposta foi {tent}.')
print('Processando....')
sleep(2)
if tent == n:
    print('\033[1;33;42m Meus parabéns você acertou em cheio!\033[m')
else:
    print('\033[1;33;41m Sinto muito, não foi desta vez.\033[m')
print (f'O número escolhido pelo computador foi o {n}')


