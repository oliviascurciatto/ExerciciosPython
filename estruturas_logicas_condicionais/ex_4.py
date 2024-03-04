"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""

letra = input('Informe uma letra: ').upper()

if letra in 'AEIOU':
    print('Essa letra é uma vogal')
else:
    print('Essa letra é uma consoante')
