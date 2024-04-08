from random import choice
a1 = input('Digite o nome do aluno:')
a2 = input('Digite o nome de outro aluno:')
a3 = input('Digite o nome de mais um aluno:')
a4 = input('Digite o nome de outro aluno:')
lista = [a1,a2,a3,a4]
win = choice(lista)
print (f'O vencedor que limpará o quadro será o aluno {win}!!!')

