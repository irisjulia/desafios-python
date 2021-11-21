'''valor = int(input())
print(valor)

notas =[100, 50, 20, 10, 5, 2, 1]

for nota in notas:
    quantnotas = int(valor/nota)
    print(f"{quantnotas} nota(s) de R$ {nota},00")

    #perguntar nere'''

n = int (input())

n100 = n//100 #o // arredonda para baixo
r = n%100 # r = resto da divisão de n por 100, o % simboliza o resto

n50 = r//50
r = r%50

n20 = r//20
r = r%20

n10 = r//10
r = r%10

n5 = r//5
r = r%5

n2 = r//2
r %= 2

n1 = r 

print (n)
print(f'{n100} nota(s) de R$ 100,00')
print(f'{n50} nota(s) de R$ 50,00')
print(f'{n20} nota(s) de R$ 20,00')
print(f'{n10} nota(s) de R$ 10,00')
print(f'{n5} nota(s) de R$ 5,00')
print(f'{n2} nota(s) de R$ 2,00')
print(f'{n1} nota(s) de R$ 1,00')