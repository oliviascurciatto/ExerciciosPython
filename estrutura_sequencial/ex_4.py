"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""

"""
Primeira resposta

notas = input('Informe as 4 notas bimestrais separadas por um espaço: ')
nota_1, nota_2, nota_3, nota_4 = notas.split()

nota_1 = int(nota_1)
nota_2 = int(nota_2)
nota_3 = int(nota_3)
nota_4 = int(nota_4)

soma = nota_1 + nota_2 + nota_3 + nota_4
media = (soma / 4)

print(f'A média bimestral é : {media}')
"""

nota1 = float(input("Digite a nota do 1º bimestre: "))
nota2 = float(input("Digite a nota do 2º bimestre: "))
nota3 = float(input("Digite a nota do 3º bimestre: "))
nota4 = float(input("Digite a nota do 4º bimestre: "))


media = (nota1 + nota2 + nota3 + nota4) / 4


print(f"A média das notas bimestrais é: {media}")
