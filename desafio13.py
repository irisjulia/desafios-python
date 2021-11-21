idade = int(input())

ano = 365
mês = 30

anos = idade//ano
r = idade%ano

meses = r//30
r = r%30

dias = r

print(f'{anos} ano(s)')
print(f'{meses} mes(es)')
print(f'{dias} dia(s)')