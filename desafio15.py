valor = (input().split())
cod = int(valor [0]) #[0] que estamos pegando a info contida no elemento 0
quant = int(valor [1])

if cod == 1:
    print(f'Total: R$ {quant*4.00:.2f}')

if cod == 2:
    print(f'Total: R$ {quant*4.50:.2f}')

if cod == 3:
    print(f'Total: R$ {quant*5.00:.2f}')

if cod == 4:
    print(f'Total: R$ {quant*2.00:.2f}')

if cod == 5:
    print(f'Total: R$ {quant*1.50:.2f}')



''' pode ser feita com o elif ou com um print direto, só atribuindo um valor fixo no total

info_lida = input().split()
codigo = int(info_lida[0])
qtd = int(info_lida[1])

if codigo == 1:
    total = 4.00*qtd
elif codigo == 2:
    total = 4.50*qtd
elif codigo == 3:
    total = 5.00*qtd
elif codigo == 4:
    total = 2.00*qtd
elif codigo == 5:
    total = 1.50*qtd

print(f'Total: R$ {total:.2f}')'''