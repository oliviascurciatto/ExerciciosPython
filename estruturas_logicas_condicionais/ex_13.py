"""
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1- domingo, 2- Segunda, etc.),
se digitar outro valor deve aparecer valor inválido.
"""

numero = input('Digite um número ')

if numero == '1':
    print('Domingo')
elif numero == '2':
    print('Segunda')
elif numero == '3':
    print('Terça')
elif numero == '4':
    print('Quarta')
elif numero == '5':
    print('Quinta')
elif numero == '6':
    print('Sexta')
elif numero == '7':
    print('Sábado')
else:
    print('Inválido')
