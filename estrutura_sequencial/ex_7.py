"""
Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
"""

print('Informe a medida do lado do quadrado: ')
lado = float(input())

quadrado = lado * lado
dobro = quadrado * 2

print(f'A área do quadrado é {quadrado}, sendo o dobro dessa área {dobro}')
