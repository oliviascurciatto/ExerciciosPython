"""
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
   F = C * 1,8 + 32
"""

print('Informe a temperatura em graus Celsius: ')
celsius = float(input())

fahrenheit = celsius * 1.8 + 32

print(f'A temperatura em Fahrenheit é: {fahrenheit}')
