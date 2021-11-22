''''salario = float(input())

if [0,400.00]:
    aumento = (0.15*salario)+salario

elif [400.01,800.00]:
    aumento = (0.12*salario)+salario

elif [800.01,1200.00]:
    aumento = (0.10*salario)+salario

elif [1200.01,2000.00]:
    aumento = (0.07*salario)+salario

else:
    aumento = (0.04*salario)+salario

if [0,400.00]:
    reajuste = aumento - salario

elif [400.01,800.00]:
    reajuste = aumento - salario

elif [800.01,1200.00]:
    reajuste = aumento - salario

elif [1200.01,2000.00]:
    reajuste = aumento - salario

else:
    reajuste = aumento - salario

if [0,400.00]:
    percentual = 15

elif [400.01,800.00]:
    percentual = 12

elif [800.01,1200.00]:
    percentual = 10

elif [1200.01,2000.00]:
    percentual = 7

else:
    percentual = 4

print(f'Novo salario: {aumento:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: {percentual} %')'
'''
salario = float(input())

if salario >= 0 and salario <= 400.00:
    aumento = (0.15*salario)+salario

elif salario >= 400.01 and salario <= 800.00:
    aumento = (0.12*salario)+salario

elif salario >= 800.01 and salario <= 1200.00:
    aumento = (0.10*salario)+salario

elif salario >= 1200.01 and salario <= 2000.00:
    aumento = (0.07*salario)+salario

else:
    aumento = (0.04*salario)+salario

if salario >= 0 and salario <= 400.00:
    reajuste = aumento - salario

elif salario >= 400.01 and salario <= 800.00:
    reajuste = aumento - salario

elif salario >= 800.01 and salario <= 1200.00:
    reajuste = aumento - salario

elif salario >= 1200.01 and salario <= 2000.00:
    reajuste = aumento - salario

else:
    reajuste = aumento - salario

if salario >= 0 and salario <= 400.00:
    percentual = 15

elif salario >= 400.01 and salario <= 800.00:
    percentual = 12

elif salario >= 800.01 and salario <= 1200.00:
    percentual = 10

elif salario >= 1200.01 and salario <= 2000.00:
    percentual = 7

else:
    percentual = 4

print(f'Novo salario: {aumento:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: {percentual} %')