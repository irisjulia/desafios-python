entrada = input().split()
h_inicial = int(entrada[0])
m_inicial = int(entrada[1])
h_final = int(entrada[2])
m_final = int(entrada[3])

total_inicial = h_inicial*60+m_inicial
total_final = h_final*60+m_final

if total_inicial < total_final:
    duracao = total_final-total_inicial
    hora = duracao//60 #transaformando em minutos
    min = duracao % 60 #o resto equivale aos minutos

if total_inicial >= total_final:
    duracao = (1440-total_inicial)+total_final #1440min é pq está tudo em minutos, 1440 é 1 dia
    hora = duracao//60 #transaformando em minutos
    min = duracao % 60 #o resto equivale aos minutos

print (f'O JOGO DUROU {hora} HORA(S) E {min} MINUTO(S)')