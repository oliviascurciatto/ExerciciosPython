"""
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão
é sempre pelo mais barato.
"""

produto_1 = float(input('Informe o preço do primeiro produto: '))
produto_2 = float(input('Informe o preço do segundo produto: '))
produto_3 = float(input('Informe o preço do terceiro produto: '))

if produto_1 < produto_2 and produto_1 < produto_3:
    mais_barato: float = produto_1
    print(f'O produto mais barato é o primeiro, que custa R$ {mais_barato:.2f}')
elif produto_2 < produto_1 and produto_2 < produto_3:
    mais_barato: float = produto_2
    print(f'O produto mais barato é o segundo, que custa R$ {mais_barato:.2f}')
else:
    mais_barato: float = produto_3
    print(f'O produto mais barato é o terceiro, que custa R$ {mais_barato:.2f}')


