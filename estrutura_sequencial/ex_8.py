"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
total do seu salário no referido mês.
"""

print('Quanto você ganha por hora?')
valor_hora = float(input())

print('Quantas horas você trabalha por mês?')
mes_horas = int(input())

salario_mes = valor_hora * mes_horas

print(f'Seu salário é de R${salario_mes} por mês')
