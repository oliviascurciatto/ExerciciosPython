"""
Faça um Programa que peça dois números e imprima a soma.
"""

"""
Primeira resposta:

print('Informe um número:')
numero_1 = input()

print('Informe outro número:')
numero_2 = input()

print(f'A soma dos dois números é: {numero_1 + numero_2}')
"""

numeros = input('Informe dois números separados por um espaço: ')

numero_1, numero_2 = numeros.split()

numero_1 = int(numero_1)
numero_2 = int(numero_2)

soma = numero_1 + numero_2

print(f'A soma dos números é: {soma}')