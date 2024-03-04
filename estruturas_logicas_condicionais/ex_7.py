"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""

numero_1 = int(input('Informe o primeiro número: '))
numero_2 = int(input('Informe o segundo número: '))
numero_3 = int(input('Informe o terceiro número: '))

if numero_1 > numero_2 and numero_1 > numero_3:
    maior = numero_1
elif numero_2 > numero_1 and numero_2 > numero_3:
    maior = numero_2
else:
    maior = numero_3

if numero_1 < numero_2 and numero_1 < numero_3:
    menor = numero_1
elif numero_2 < numero_1 and numero_2 < numero_3:
    menor = numero_2
else:
    menor = numero_3

print(f'O maior número é {maior}')
print(f'O menor número é {menor}')
