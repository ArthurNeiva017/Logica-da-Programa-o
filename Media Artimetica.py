# Media Aritimetica


cont_qtd = 0
qtd = int(input('Quantos números deseja calcular a média aritimetica? '))
for i in range(qtd):
    cont_qtd += 1
    num = int(input('Digite o número desejado: '))

Ma = num / cont_qtd

print(f'A média aritimetica é {Ma}')