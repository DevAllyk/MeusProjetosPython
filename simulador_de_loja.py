# Simulador de pagamento de lojas

print('{:=^40}'.format(' Lojas Carvalho '))
valor_produto = float(input('Preço das compras: R$'))
pagamento = int(input('''Escolha uma opção de pagamento:
[ 1 ] Á vista dinheiro/cheque
[ 2 ] Á vista no Cartão
[ 3 ] 2x no Cartão
[ 4 ] 3x ou mais no Cartão
'''))
if pagamento == 1:
    total = valor_produto - (10 / 100 * valor_produto)
    print('Você irá pagar R${:.2f} com 10% de Desconto!'.format(total))
elif pagamento == 2:
    total = valor_produto - (5 / 100 * valor_produto)
    print('Você irá pagar R${:.2f} com 5% de Desconto!'.format(total))
elif pagamento == 3:
    print('Você irá pagar R${:.2f}, Sem Juros!'.format(valor_produto))
elif pagamento == 4:
    total = valor_produto + (20 / 100 * valor_produto)
    parcela = int(input('Deseja parcelar em quantas vezes? '))
    valor_total = total / parcela
    print('Você pagará o valor de R${:.2f} parcelado em {}x.'.format(valor_total, parcela))
    print('O valor total das sua compras será R${:.2f}, COM JUROS!'.format(total))
else:
    print('Por favor, Digitar uma opção válida!')