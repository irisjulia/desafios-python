entrada = float(input())
while entrada < 0 or entrada > 10:
    print('nota invalida')
    entrada = float(input())
    if entrada >= 0 and entrada <=10:
        entrada_2 = float(input())
while entrada_2 < 0 or entrada_2 >10:
    print('nota invalida')
    entrada_2 = float(input())
if entrada_2 >= 0 and entrada_2 <= 10:
    print(f'media = {(entrada+entrada_2)/2:.2f}')