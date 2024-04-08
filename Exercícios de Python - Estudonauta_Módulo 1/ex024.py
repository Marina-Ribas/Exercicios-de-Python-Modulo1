cidade = input('Digite o nome de uma cidade:').upper().strip()
santo = cidade [0:5]=="SANTO"
if santo is True:
    print('Sua cidade começa com o nome Santo.')
else:
    print('Sua cidade não começa com o nome Santo.')


