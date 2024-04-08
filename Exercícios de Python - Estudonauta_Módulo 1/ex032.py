#O ano é bissexto quando ele não é divisil por 100 e divisil por 4 ou é divisivel por 400.

from datetime import date
ano = int(input('Digite o ano: Coloque 0 para analisar o ano atual:'))
if ano == 0:
    ano = date.today().year
if ano % 100 != 0 and ano % 4 ==0 or ano % 400== 0:
    print(f'O ano {ano} é Bissexto')
else:
    print(f'O ano {ano} não é Bissexto.')
