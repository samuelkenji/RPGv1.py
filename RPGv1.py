from random import randint
hp0=100
hp_mob=50
r_encounter=int(randint(0,100))
if r_encounter<35:
    print('Um inimigo se aproxima')
    decisao=int(input('1-Atacar   2-Defender    3-Fugir: '))
    if decisao==1:
        combate=int(randint(1,20))
        if combate<10:
            hp_mob1=hp_mob-5
            print('Você deu 5 de dano')
        elif combate>10 and combate<20:
            hp_mob1 = hp_mob -10
            print('Você deu 10 de dano')
        else:
            hp_mob1 = hp_mob -20
            print('Ataque crítico! 20 de dano')
    elif decisao==2:
        defesa=int(randint(1,20))
        if defesa<5:
            hp1=hp0-5
            print('Sua defesa falhou')
        else:
            print('Você bloqueou o ataque com sucesso!')
    elif decisao==3:
        fuga=int(randint(1,20))
        if fuga<4:
            print('Parace que algúem não quer que você fuja')
        else:
            print('Você escapou com sucesso')