valor = float(input('Digite o valor do produto: R$ '))
print('''Formas de pagamento:
[1] à vista dinheiro/cheque: 10% de desconto
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão: 20% de juros''')
escolha = int(input('Qual é a opção? '))
if escolha == 1:
    preco = valor - 0.1 * valor
    print('Pagamento à vista em dinheiro ou cheque com 10% de desconto. Valor total de R$ {:.2f}'.format(preco))
elif escolha == 2:
    preco = valor
    print('Pagamento à vista no cartão. Valor total de R$ {:.2f}'.format(preco))
elif escolha == 3:
    preco = valor / 2
    print('Pagamento em duas parcelas de R$ {:.2f}'.format(preco))
elif escolha == 4:
    preco = valor + 0.2 * valor
    parcela = preco / 3
    print('Pagamento total de R$ {:.2f} a ser efetuado em 3 parcelas de R$ {:.2f}'.format(preco, parcela))


