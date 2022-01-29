#Verifica se o nome da cidade começa com a palavra Santo

cidade = str(input('Digite o nome de uma cidade: ')).strip().split()
print(cidade[0].upper() == 'SANTO')


