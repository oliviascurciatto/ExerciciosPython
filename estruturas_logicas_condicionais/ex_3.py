"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
F - Feminino, M - Masculino, Sexo Inválido.
"""

letra = input('Digite uma letra: ').upper()


if letra == 'M':
    print('M - Masculino')
elif letra == 'F':
    print('F - Feminino')
else:
    print('Letra Inválida')
