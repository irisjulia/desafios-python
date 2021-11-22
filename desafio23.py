salario = float(input())

if salario >= 0.00 and salario <= 2000.00:
    print('Isento')

if salario >= 2000.01 and salario<= 3000.00:
    a = (salario-2000.00)*0.08
    print(f'R$ {x:.2f}')
    
if salario >= 3000.01 and salario <= 4500.00:
    a = 1000*0.08
    b = (salario-2000-1000)*0.18
    print(f'R$ {a+b:.2f}')

if salario > 4500:
    a = 1000*0.08
    b = 1500 * 0.18
    c = (salario - 2000 - 1000 - 1500)*0.28
    print(f'R$ {a+b+c:.2f}')