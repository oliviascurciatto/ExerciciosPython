"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas
de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
    - Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    - comprar apenas latas de 18 litros;
    - comprar apenas galões de 3,6 litros;
    - misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre
     arredonde os valores para cima, isto é, considere latas cheias.
"""
import math

area = float(input('Qual é a metragem da área a ser pintada?'))

litro_tinta = area / 6
quantidade_latas_grande = litro_tinta / 18
quantidade_latas_pequena = litro_tinta / 3.6

preco_lata_grande = quantidade_latas_grande * 80.00
preco_lata_pequena = quantidade_latas_pequena * 25.00

latas_grandes_mistura = math.ceil((litro_tinta * 1.1) / 18)
latas_pequenas_mistura = math.ceil((litro_tinta * 1.1) / 3.6)
preco_total_mistura = (latas_grandes_mistura * 80.00) + (latas_pequenas_mistura * 25.00)


print(f"Quantidade de latas grandes de tinta a serem compradas: {quantidade_latas_grande}")
print(f"Preço total: R$ {preco_lata_grande:.2f}")

print(f"Quantidade de latas pequenas de tinta a serem compradas: {quantidade_latas_pequena}")
print(f"Preço total: R$ {preco_lata_pequena:.2f}")


print(f"Melhor combinação de latas e galões:")
print(f" - Quantidade de latas de 18 litros: {latas_grandes_mistura}")
print(f" - Quantidade de galões de 3,6 litros: {latas_pequenas_mistura}")
print(f" - Preço total da mistura: R$ {preco_total_mistura:.2f}")