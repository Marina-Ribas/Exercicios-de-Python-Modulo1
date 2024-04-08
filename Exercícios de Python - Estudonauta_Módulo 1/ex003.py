n1 = int(input('Digite um número'))
n2 = int(input('Digite outro número'))
s = n1 + n2
print('A soma entre {} e {} é igual a {}'.format(n1,n2,s))



#Depois da versão 3.7 do python não precisa mais usar .format (), apenas coloque um f antes das aspas " " e
# escreva o nome da variavel dentro dos colchetes {}  exemplo: print (f'A soma de {n1} e {n2} é {s}')