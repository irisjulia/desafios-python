'''entrada = (input().split())
n1 = int(entrada[0])
n2 = int(entrada[1])
n3 = int(entrada[2])

lista = [n1, n2, n3]
lista.sort()

for i in lista: #essa função permite que ele imprima com quebra de linha
    print(i)

print("")

lista.sort(reverse=True)
for i in lista:
    print(i)'''

entrada = (input().split())
n1 = int(entrada[0])
n2 = int(entrada[1])
n3 = int(entrada[2])

lista = [n1, n2, n3]
lista.sort()

for i in lista: #essa função permite que ele imprima com quebra de linha
    print(i)

print("")
print(n1, n2, n3, sep="\n") #o \n é usado para quebrar linha