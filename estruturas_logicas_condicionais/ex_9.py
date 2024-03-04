"""
Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""

"""
numero_1 = int(input('Informe o primeiro número: '))
numero_2 = int(input('Informe o segundo número: '))
numero_3 = int(input('Informe o terceiro número: '))

if numero_1 <= numero_2 and numero_1 <= numero_3:
    menor = numero_1
    if numero_2 <= numero_3:
        meio = numero_2
        maior = numero_3
elif numero_2 <= numero_1 and numero_2 <= numero_3:
    menor = numero_2
    if numero_3 <= numero_1:
        meio = numero_3
        maior = numero_1
else:
    menor = numero_3
    if numero_1 <= numero_2:
        meio = numero_1
        maior = numero_2

print(f'Os números em ordem decrescente ficam: {maior} {meio} {menor} ')
"""

numero_1 = int(input('Informe o primeiro número: '))
numero_2 = int(input('Informe o segundo número: '))
numero_3 = int(input('Informe o terceiro número: '))

if numero_1 <= numero_2 and numero_1 <= numero_3:
    menor = numero_1
    if numero_2 <= numero_3:
        meio = numero_2
        maior = numero_3
    else:
        meio = numero_3
        maior = numero_2
elif numero_2 <= numero_1 and numero_2 <= numero_3:
    menor = numero_2
    if numero_3 <= numero_1:
        meio = numero_3
        maior = numero_1
    else:
        meio = numero_1
        maior = numero_3
else:
    if numero_1 >= numero_2 and numero_1 >= numero_3:
        maior = numero_1
        if numero_2 >= numero_3:
            meio = numero_2
            menor = numero_3
        else:
            meio = numero_3
            menor = numero_2
    elif numero_2 >= numero_1 and numero_2 >= numero_3:
        maior = numero_2
        if numero_3 >= numero_1:
            meio = numero_3
            menor = numero_1
        else:
            meio = numero_1
            menor = numero_3
    else:
        maior = numero_3
        if numero_1 >= numero_2:
            meio = numero_1
            menor = numero_2
        else:
            meio = numero_2
            menor = numero_1

print(f'Os números em ordem decrescente ficam: {maior} {meio} {menor}')
