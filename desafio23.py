salario = float(input())

if salario >= 0.00 and salario <= 2000.00:
    print('Isento')

if salario >= 2000.01 and salario<= 3000.00:
    x = (salario-2000.00)*0.08
    print(f'R$ {x:.2f}')
    
if salario >= 3000.01 and salario <= 4500.00:
    x = 

