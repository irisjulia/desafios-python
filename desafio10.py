#nome do vendedor (string), salário (float) e montante total vendas (float)

"""nome = str(input())
salario = float(input())
total_vendas = float(input())

total = total_vendas*0,15
salario1 = float(total + salario)

print(f"TOTAL = R$ {salario1:.2f}")"""


nome = input()
salario = float(input())
vendas = float(input())

comissao = (vendas*0.15)
salario=(salario+comissao)

print(f"TOTAL = R$ {salario:.2f}")

