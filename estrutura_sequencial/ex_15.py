"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o
total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5%
para o sindicato, faça um programa que nos dê:
    1. Salário bruto.
    2. quanto pagou ao INSS.
    3. quanto pagou ao sindicato.
    4. o salário líquido.
    5. calcule os descontos e o salário líquido, conforme a tabela abaixo.
    Obs.: Salário Bruto - Descontos = Salário Líquido.
"""

valor_hora = float(input('Qual é o valor da sua hora de trabalho?'))
horas_trabalhadas = float(input('Quantas horas você trabalha por mês?'))

salario_bruto = valor_hora * horas_trabalhadas


inss = salario_bruto * 0.08
ir = salario_bruto * 0.11
sindicato = salario_bruto * 0.05

salario_liquido = salario_bruto - inss - ir - sindicato


print(f'Seu salário bruto é: {salario_bruto}')
print(f'Seu salário no final do mês, com os descontos de IR, INSS e Sindicato é: {salario_liquido: .2f}')
