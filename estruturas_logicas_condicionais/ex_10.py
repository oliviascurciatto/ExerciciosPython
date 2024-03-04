"""
Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""

periodo = (input('Em qual período você estuda? Responda com M para matutino, V para vespertino ou N para noturno.')
           .upper())

if periodo in 'M':
    print('Bom dia!')
elif periodo in 'V':
    print('Boa tarde!')
elif periodo in 'N':
    print('Boa noite!')
else:
    print('Período inválido')
