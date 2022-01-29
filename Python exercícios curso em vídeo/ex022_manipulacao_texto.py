nome = str(input('Digite seu nome: ')).strip()
print('NOME: {}'.format(nome.upper()))
print('nome: {}'.format(nome.lower()))
print('Quantidade de letras = {}'.format(len(nome)-nome.count(' ')))
#forma mais fácil → print('Quantidade de letras do primeiro nome = {}'.format(nome.find(' ')))


#forma mais dificil → separa = nome.split()
#print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

