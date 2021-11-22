entrada = (input().split())

n1 = float(entrada [0])
n2 = float(entrada [1])
n3 = float(entrada [2])
n4 = float(entrada [3])

media = (n1*2 + n2*3 + n3*4 + n4*1)/10
print(f'Media: {media:.1f}')

if media >= 7.0:
    print("Aluno aprovado.")

elif media < 5.0:
    print("Aluno reprovado.") #o elif para de executar quando acha uma condição verdadeira

elif 5 <= media < 7.0:
    print("Aluno em exame.") 
    exame = float(input())
    print(f'Nota do exame: {exame:.1f}')
    media_exame = (exame + media)/2
    if media_exame >= 5.0:
        print("Aluno aprovado.")
    if media_exame < 5.0:
        print("Aluno reprovado.")
    print(f'Media final: {media_exame:.1f}')