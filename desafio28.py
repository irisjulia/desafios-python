n = int(input())
if 5 < n < 2000:
    for i in range (2,n+1,2):
        saida = i**2
        print(f'{i}^2 = {saida}')
