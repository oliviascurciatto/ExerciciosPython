"""
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
    - C = 5 * ((F-32) / 9).
"""

print('Informe a temperatura em Fahrenheit: ')
fahrenheit = float(input())

celcius = 5 * ((fahrenheit - 32) / 9)

print(f'A temperatura em graus Celsius é: {celcius}')
