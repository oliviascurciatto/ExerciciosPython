"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""

arquivo = float(input('Informe o tamanho do arquivo:'))
velocidade_link = float(input('Informe a velocidade do link:'))

download_em_segundos = arquivo / velocidade_link

download_em_minutos = download_em_segundos / 60

print(f'O arquivo levará {download_em_minutos: .2f} minutos para ser baixado')
