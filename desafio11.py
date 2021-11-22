#pesquisar como usar a função lista
"""peça1 = input().split()
peça2 = input().split()

peça1 = codigo1,quantidade1,valor1
peça2 = codigo2,quantidade2,valor2

total = ((int(quantidade1)+float(valor1))*((int(quantidade2)+float(valor2))

valor a pagar = (f"VALOR A PAGAR: R${total:.2f")"""

linha1= input().split()
codigo1 = int(linha1[0])
numerop1 = int(linha1[1])
valor1 = float(linha1[2])

linha2= input().split()
codigo2 = int(linha2[0])
numerop2 = int(linha2[1])
valor2 = float(linha2[2])

total = numerop1*valor1 + numerop2*valor2

print(f"VALOR A PAGAR: R$ {total:.2f}")