from random import randint
hp0=100
hp_mob1=50
r_encounter=int(randint(0,100))
if r_encounter<35:
    print('Um inimigo se aproxima')
    decisao=input('Atacar   Defender    Fugir')
    if decisao='Atacar' or decisao='atacar':
        combate=int(randint(1,20))
        if combate<10:
            hp1=hp0-10
            print('Você perdeu 10 de vida')
        elif combate>10 and combate<20:
            print('Você deu 10 de dano')
        else:
            print('Ataque crítico! 20 de dano')
    elif decisao='Defender' or decisao='defender':
        defesa=int(randint(1,20))
        if defesa<10:
            hp1=hp0-5
            print('Sua defesa falhou')
        else:
            print('Você bloqueou o ataque com sucesso!')