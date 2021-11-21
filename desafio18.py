
entrada = input().split()
hora_inicio = int(entrada[0])
fim_jogo = int(entrada[1])

if fim_jogo > hora_inicio:
    print(f'O JOGO DUROU {fim_jogo - hora_inicio} HORA(S)')


elif fim_jogo < hora_inicio:
    horas = (24 - hora_inicio + fim_jogo)
    print(f'O JOGO DUROU {horas} HORA(S)')

elif fim_jogo == hora_inicio:
    horas = (hora_inicio - fim_jogo + 24)
    print(f'O JOGO DUROU {horas} HORA(S)')