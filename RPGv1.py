from random import randint
hp0=100
pot=1
pts=0
fugiu=0

nome=input('Qual seu nome?:')
bif=(input('Você entra na masmorra e logo se depara com uma bifurcação.\nDeseja ir pela esquerda ou direita?:'))

while hp0 > 0:
    if bif=='esquerda' or bif=='Esquerda':
            mob_encounter=int(randint(0,100))
            ataque_mob=randint(1,10)
            if mob_encounter<35:
                hp_mob1 = 50
            elif mob_encounter>75:
                hp_mob1=60
            print('Um inimigo se aproxima')
            while hp_mob1 > 0:
                print('Mob: {}  Você: {}'.format(hp_mob1,hp0))
                decisao = int(input('1-Atacar   2-Defender    3-Fugir     4-Item: '))
                if decisao == 1:
                    combate = int(randint(1, 20))
                    if combate < 10 and combate>4:
                        hp_mob1 = hp_mob1 - 5
                        print('Você deu 5 de dano')
                        print('O inimigo ataca de volta te dando {} de dano.'.format(ataque_mob))
                        hp0=hp0-ataque_mob
                    elif combate < 3:
                        print('Errou!')
                        print('O inimigo ataca de volta te dando {} de dano'.format(ataque_mob))
                        hp0=hp0-ataque_mob
                    elif combate > 10 and combate < 20:
                        hp_mob1 = hp_mob1 - 10
                        print('Você deu 10 de dano')
                        print('O inimigo ataca de volta te dando {} de dano'.format(ataque_mob))
                        hp0=hp0-ataque_mob
                    else:
                        hp_mob1 = hp_mob1 - 20
                        print('Ataque crítico! 20 de dano')
                        print('O inimigo ataca de volta te dando {} de dano'.format(ataque_mob))
                        hp0=hp0-ataque_mob
                elif decisao == 2:
                    defesa = int(randint(1, 20))
                    if defesa < 5:
                        hp0 = hp0 - 5
                        print('Sua defesa falhou')
                        print('Você levou 5 de dano')
                    else:
                        print('Você bloqueou o ataque com sucesso!')
                elif decisao == 3:
                    fuga = int(randint(1, 20))
                    if fuga < 4:
                        print('Parece que algúem não quer que você fuja')
                    else:
                        print('Você escapou com sucesso')
                        fugiu=fugiu+1
                        if fugiu==1:
                            break
                elif decisao == 4:
                    print('Qual item você deseja usar?')
                    inv=int(input('Inventário:\n    1-Poção - {}    2-Voltar'.format(pot)))
                    if inv==1:
                        if pot>=1:
                            hp0=hp0+25
                            print('Você recuperou 25 de vida')
                        else:
                            print('Você não tem poções')
            if fugiu==1:
                print('Você ganhou 100 pontos!')
                pts=pts+100
            else:
                print('Você ganhou 200 pontos!')
                pts=pts+200
    if bif=='direita' or bif=='Direita':
        bau=int(randint(0,100))
        if bau<20:
            print('Você encontrou um baú. Deseja abri-lo?')
            trap=int(randint(0,100))
            if trap<15:
                print('Era uma armadilha!')
                print('Você levou 5 de dano')
                hp0=hp0-5
            elif trap>15 and trap<100:
                print('Você achou uma poção!')
                pot=pot+1
            else:
                print('Você achou duas poções!')
                pot=pot+2
    print('Você se depara com um enorme lago')
    lago=input('Ao olhar mais de perto percebe que há um brilho misterioso vindo do fundo dele\nDeseja investigar? S/N')
    if lago=='s' or lago=="S":
        trap2=int(randint(0,100))
        if trap2<30:
            hp_mob2 = 35
        elif trap2>75:
            hp_mob2=50
        print('Era o brilho de um monstro aquático!')
        while hp_mob2 > 0:
            ataque_mob2=randint(1,15)
            print('Mob: {}  Você: {}'.format(hp_mob2, hp0))
            decisao = int(input('1-Atacar   2-Defender    3-Fugir     4-Item: '))
            if decisao == 1:
                combate = int(randint(1, 20))
                if combate < 10 and combate>4:
                    hp_mob2 = hp_mob2 - 5
                    print('Você deu 5 de dano')
                    print('O inimigo ataca de volta te dando {} de dano.'.format(ataque_mob2))
                    hp0 = hp0 - ataque_mob2
                elif combate < 3:
                    print('Errou!')
                elif combate > 10 and combate < 20:
                    hp_mob2 = hp_mob2 - 10
                    print('Você deu 10 de dano')
                    print('O inimigo ataca de volta te dando {} de dano.'.format(ataque_mob2))
                    hp0 = hp0 - ataque_mob2
                else:
                    hp_mob2 = hp_mob2 - 20
                    print('Ataque crítico! 20 de dano')
                    print('O inimigo ataca de volta te dando {} de dano.'.format(ataque_mob2))
                    hp0 = hp0 - ataque_mob2
            elif decisao == 2:
                defesa = int(randint(1, 20))
                if defesa < 5:
                    hp1 = hp0 - 5
                    print('Sua defesa falhou')
                    print('Você levou 5 de dano')
                else:
                    print('Você bloqueou o ataque com sucesso!')
            elif decisao == 3:
                fuga = int(randint(1, 20))
                if fuga < 4:
                    print('Parece que algúem não quer que você fuja')
                else:
                    print('Você escapou com sucesso')
                    fugiu = 1
                    if fugiu == 1:
                        break
            elif decisao == 4:
                print('Qual item você deseja usar?')
                inv = int(input('Inventário:\n    1-Poção - {}    2-Voltar'.format(pot)))
                if inv == 1:
                    if pot >= 1:
                        hp0 = hp0 + 25
                        print('Você recuperou 25 de vida')
                    else:
                        print('Você não tem poções')
        if fugiu == 1:
            print('Você ganhou 100 pontos!')
            pts = pts + 100
        else:
            print('Você ganhou 200 pontos!')
            pts = pts + 200


print('Você perdeu')
print(nome)
print('{} pontos'.format(pts))
