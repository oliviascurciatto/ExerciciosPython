"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro_tinta para cada 3 metros quadrados e que a tinta é vendida em latas de
18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""

area = float(input('Qual é a metragem da área a ser pintada?'))


litro_tinta = area / 3

quantidade_latas = litro_tinta / 18

quantidade_latas = int(quantidade_latas) if quantidade_latas == int(quantidade_latas) else int(quantidade_latas) + 1


preco_total = quantidade_latas * 80.00

print(f"Quantidade de latas de tinta a serem compradas: {quantidade_latas}")
print(f"Preço total: R$ {preco_total:.2f}")
