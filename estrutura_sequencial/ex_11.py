"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    a. o produto do dobro do primeiro com metade do segundo.
    b. a soma do triplo do primeiro com o terceiro.
    c. o terceiro elevado ao cubo.
"""

print('Informe um número inteiro: ')
num_1 = int(input())

print('Informe outro número inteiro: ')
num_2 = int(input())

print('Informe um número real: ')
num_3 = float(input())

questao_a = ((num_1 * 2) ** 2) + (num_2 / 2)
print(f'o produto do dobro do primeiro com metade do segundo é: {questao_a}')

questao_b = (num_1 * 3) + num_3
print(f'a soma do triplo do primeiro com o terceiro é: {questao_b}')

questao_c = num_3 ** 3
print(f'o terceiro elevado ao cubo é: {questao_c}')
