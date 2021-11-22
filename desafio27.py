x = 0
y = 0

for n in range(6):
    valor = float(input())
    if valor >= 0:
        x+=1 
        y+=valor
        media = y/x
print(f'{x} valores positivos\n{media:.1f}')