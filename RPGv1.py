#Lucas Quental e Samuel Kenji
from random import randint
import time
hp0=100
pot=1
pts=0
fugiu=0
fugiu2=0
fugiu3=0
fugiu4=0
drop=randint(0,100)

manual=('Manual do jogo: '
'-->Na hora de fazer suas escolhas sempre veja suas opções \n'
'-->Seu HP no inicio do jogo será de 100 \n'
'-->O jogador começará com uma poção nos itens \n'
'-->É possível encontrar mais poções no decorrer do jogo\n'
'-->O jogador terá as opções de Atacar, Defender, Fugir e utilizar um Item \n'
'-->Quando o HP do jogador chegar a 0 ele perde o jogo \n'
'-->Ao matar um Mob o jogador ganha 200 Pontos e ao fugir com sucesso, 200 pontos \n'
'-->Este jogo é livre para todos os públicos'
        )
print(manual)
print(input('Aperte Enter para iniciar...'))

diario=('Dia 14: Já fazem 2 semanas que meu irmão esta desaparecido. A última coisa que me lembro é dele dizendo que estava indo para a Gerudo Valley...\n'
'Após o 3° dia do seu desaparecimento decidi ir em busca dele. Juntei minhas coisas e fui pela velha estrada de Victory Road.\n'
'A estrada era totalmente deserta porém com árvores muito densas ao redor.\n'
'Em um determinado momento caí em um buraco e machuquei minha perna, porém consegui escalar para fora do buraco, quando de repente...')
print(diario)

print ("Desconhecido : Ei você! Precisa de ajuda? Meu nome é Papaco.")
time.sleep(2)
print ("Papaco : Qual o seu nome?")
nome=input('->').title()
time.sleep(0.5)
print ("Papaco : Olá", nome,",parece que você procura por algo")
time.sleep(2)
print ("Papaco : Pelo jeito você é um forasteiro.")
time.sleep(2)
print ("Papaco : Está aqui atrás de que?")
time.sleep(2.5)
print ('->',nome, ": Estou atrás do meu irmão perdido.")
time.sleep(2)
print ('->',nome, ": Ele sumiu faz alguns dias, mas antes disse que ia para a cidade de Gerudo Valley...")
time.sleep(3)
print ("Papaco : Talvez ele possa ter ido pelas masmorras, é o caminho mais rapido para a cidade de Gerudo Valley.")
time.sleep(3)
print ("Papaco : As masmorras ficam naquela direção. Apenas tenha cuidado em sua jornada.")
time.sleep(3)
print ("Papaco : Existem várias criaturas que moram nas redondezas.")
time.sleep(2.5)
print ("Papaco : Por segurança leve minha espada, meu escudo e minha poção.")
time.sleep(2.5)
print ("Papaco : Faça bom uso desses equipamentos e boa sorte em sua jornada jovem", nome,".")
time.sleep(2)
bif=(input('Então, eu entrei na masmorra e logo me deparo com uma bifurcação.\nDeseja ir para qual lado?\n1-Esquerda  2-Direita:\n->'))
time.sleep(0.25)


while hp0 > 0:
    if bif=='esquerda' or bif=='1':
            mob_encounter=int(randint(0,100))
            ataque_mob=randint(4,10)
            if mob_encounter<35:
                hp_mob1 = 50
            elif mob_encounter>75:
                hp_mob1=60
            else:
                hp_mob1=55
            print('Pouco tempo depois de entrar, um esqueleto se aproximou brandando uma espada enferrujada')
            time.sleep(0.25)
            while hp_mob1 > 0:
                if hp0 < 0:
                    break
                print('Mob: {}  Você: {}'.format(hp_mob1,hp0))
                time.sleep(0.25)
                decisao = int(input('1-Atacar   2-Defender    3-Fugir     4-Item:\n-> '))
                time.sleep(0.25)
                if decisao == 1:
                    combate = int(randint(1, 20))
                    if combate < 10 and combate>4:
                        hp_mob1 = hp_mob1 - 5
                        print('Você deu 5 de dano')
                        time.sleep(0.5)
                        print('O inimigo ataca de volta te dando {} de dano.'.format(ataque_mob))
                        hp0=hp0-ataque_mob
                    elif combate < 3:
                        print('Errou!')
                        time.sleep(0.5)
                        print('O inimigo ataca de volta te dando {} de dano'.format(ataque_mob))
                        hp0=hp0-ataque_mob
                    elif combate > 10 and combate < 18:
                        hp_mob1 = hp_mob1 - 10
                        print('Você deu 10 de dano')
                        time.sleep(0.5)
                        print('O inimigo ataca de volta te dando {} de dano'.format(ataque_mob))
                        hp0=hp0-ataque_mob
                    else:
                        hp_mob1 = hp_mob1 - 20
                        print('Ataque crítico! 20 de dano')
                        time.sleep(0.5)
                        print('O inimigo ataca de volta te dando {} de dano'.format(ataque_mob))
                        hp0=hp0-ataque_mob
                elif decisao == 2:
                    defesa = int(randint(1, 20))
                    if defesa < 5:
                        hp0 = hp0 - 5
                        print('Sua defesa falhou')
                        time.sleep(0.5)
                        print('Você levou 5 de dano')
                    else:
                        time.sleep(0.25)
                        print('Você bloqueou o ataque com sucesso!')
                elif decisao == 3:
                    fuga = int(randint(1, 20))
                    if fuga < 4:
                        print('Parece que algúem não quer que você fuja')
                        time.sleep(0.5)
                        print('Você levou 5 de dano')
                        hp0=hp0 -5
                    else:
                        print('Você escapou com sucesso')
                        time.sleep(0.25)
                        fugiu=fugiu+1
                        if fugiu==1:
                            break
                elif decisao == 4:
                    print('Qual item você deseja usar?')
                    time.sleep(0.25)
                    inv=int(input('Inventário:\n    1-Poção - {}    2-Voltar\n->'.format(pot)))
                    if inv==1:
                        if pot>=1:
                            hp0=hp0+25
                            time.sleep(0.25)
                            print('Você recuperou 25 de vida')
                        else:
                            time.sleep(0.25)
                            print('Você não tem poções')
            if fugiu==1:
                time.sleep(0.25)
                print('Você ganhou 100 pontos!')
                pts=pts+100
            else:
                time.sleep(0.25)
                print('Você ganhou 200 pontos!')
                pts=pts+200
                if drop<25:
                    pot=pot+1
                    time.sleep(0.25)
                    print('Você encontra uma poção junto ao cadáver')
    if bif=='direita' or bif=='2':
        bau=int(randint(0,50))
        if bau<20:
            bau_abrir=input('Você encontrou um baú. Deseja abri-lo? (S/N)\n-> ').upper()
            if bau_abrir=='S':
                trap=int(randint(0,100))
                if trap<15:
                    time.sleep(0.25)
                    print('Era uma armadilha!')
                    time.sleep(0.5)
                    print('Você levou 5 de dano')
                    hp0=hp0-5
                    if hp0 < 0:
                        break
                elif trap>15 and trap<100:
                    time.sleep(0.25)
                    print('Você achou uma poção!')
                    pot=pot+1
                else:
                    time.sleep(0.25)
                    print('Você achou duas poções!')
                    pot=pot+2
            elif bau_abrir=='N':
                time.sleep(0.25)
                print('Melhor prevenir do que remediar, não é mesmo?')
    if hp0 < 0:
        break
    time.sleep(0.5)
    print('Mais ao fim da primeira grande seção me deparo com um grande lago')
    time.sleep(0.5)
    lago=input('Ao olhar mais de perto percebo que há um brilho misterioso vindo do fundo dele\nDeseja investigar? (S/N)\n->').upper()
    if lago=="S":
        trap2=int(randint(0,100))
        if trap2<30:
            hp_mob2 = 35
        elif trap2>75:
            hp_mob2=50
        else:
            hp_mob2=55
        time.sleep(0.25)
        print('Era o brilho de um monstro aquático!')
        time.sleep(0.25)
        while hp_mob2 > 0:
            if hp0 < 0:
                break
            ataque_mob2=randint(5,15)
            print('Mob: {}  Você: {}'.format(hp_mob2, hp0))
            time.sleep(0.25)
            decisao = int(input('1-Atacar   2-Defender    3-Fugir     4-Item:\n-> '))
            time.sleep(0.25)
            if decisao == 1:
                combate = int(randint(1, 20))
                if combate < 10 and combate>4:
                    hp_mob2 = hp_mob2 - 5
                    print('Você deu 5 de dano')
                    time.sleep(0.5)
                    print('O inimigo ataca de volta te dando {} de dano.'.format(ataque_mob2))
                    hp0 = hp0 - ataque_mob2
                elif combate < 3:
                    print('Errou!')
                elif combate > 10 and combate < 18:
                    hp_mob2 = hp_mob2 - 10
                    print('Você deu 10 de dano')
                    time.sleep(0.5)
                    print('O inimigo ataca de volta te dando {} de dano.'.format(ataque_mob2))
                    hp0 = hp0 - ataque_mob2
                else:
                    hp_mob2 = hp_mob2 - 20
                    print('Ataque crítico! 20 de dano')
                    time.sleep(0.5)
                    print('O inimigo ataca de volta te dando {} de dano.'.format(ataque_mob2))
                    hp0 = hp0 - ataque_mob2
            elif decisao == 2:
                defesa = int(randint(1, 20))
                if defesa < 5:
                    hp1 = hp0 - 5
                    print('Sua defesa falhou')
                    time.sleep(0.5)
                    print('Você levou 5 de dano')
                else:
                    print('Você bloqueou o ataque com sucesso!')
            elif decisao == 3:
                fuga = int(randint(1, 20))
                if fuga < 4:
                    print('Parece que algúem não quer que você fuja')
                    time.sleep(0.5)
                    print('Você levou 5 de dano')
                    hp0=hp0-5
                else:
                    print('Você escapou com sucesso')
                    fugiu2 = 1
                    if fugiu2 == 1:
                        break
            elif decisao == 4:
                print('Qual item você deseja usar?')
                time.sleep(0.25)
                inv = int(input('Inventário:\n    1-Poção - {}    2-Voltar\n->'.format(pot)))
                if inv == 1:
                    if pot >= 1:
                        hp0 = hp0 + 25
                        time.sleep(0.25)
                        print('Você recuperou 25 de vida')
                    else:
                        time.sleep(0.25)
                        print('Você não tem poções')
        if fugiu == 2:
            time.sleep(0.25)
            print('Você ganhou 100 pontos!')
            pts = pts + 100
        else:
            time.sleep(0.25)
            print('Você ganhou 200 pontos!')
            pts = pts + 200
            if drop<15:
                time.sleep(0.25)
                print('Você achou uma poção junto ao cadáver')
                pot=pot+1
    else:
        time.sleep(0.25)
        lago2=(input('Um barulho muito estranho emana do lago. Deseja ignorá-lo mesmo assim? (S/N)\n->')).upper()
        if lago2=='N':
            ataque_mob=randint(5,15)
            trap2=int(randint(0,100))
            if trap2<30:
                hp_mob2 = 35
            elif trap2>75:
                hp_mob2=50
            else:
                hp_mob2=55
            time.sleep(0.25)
            print('Um monstro emergiu do lago!')
            time.sleep(0.25)
            while hp_mob2 > 0:
                if hp0 < 0:
                    break
                print('Mob: {}  Você: {}'.format(hp_mob2,hp0))
                time.sleep(0.25)
                decisao = int(input('1-Atacar   2-Defender    3-Fugir     4-Item:\n->'))
                time.sleep(0.25)
                if decisao == 1:
                    combate = int(randint(1, 20))
                    if combate < 10 and combate>4:
                        hp_mob2 = hp_mob2 - 5
                        print('Você deu 5 de dano')
                        time.sleep(0.5)
                        print('O inimigo ataca de volta te dando {} de dano.'.format(ataque_mob))
                        hp0=hp0-ataque_mob
                    elif combate < 3:
                        print('Errou!')
                        time.sleep(0.5)
                        print('O inimigo ataca de volta te dando {} de dano'.format(ataque_mob))
                        hp0=hp0-ataque_mob
                    elif combate > 10 and combate < 18:
                        hp_mob2 = hp_mob2 - 10
                        print('Você deu 10 de dano')
                        time.sleep(0.5)
                        print('O inimigo ataca de volta te dando {} de dano'.format(ataque_mob))
                        hp0=hp0-ataque_mob
                    else:
                        hp_mob2 = hp_mob2 - 20
                        print('Ataque crítico! 20 de dano')
                        time.sleep(0.5)
                        print('O inimigo ataca de volta te dando {} de dano'.format(ataque_mob))
                        hp0=hp0-ataque_mob
                elif decisao == 2:
                    defesa = int(randint(1, 20))
                    if defesa < 5:
                        hp0 = hp0 - 5
                        print('Sua defesa falhou')
                        time.sleep(0.5)
                        print('Você levou 5 de dano')
                    else:
                        print('Você bloqueou o ataque com sucesso!')
                elif decisao == 3:
                    fuga = int(randint(1, 20))
                    if fuga < 4:
                        print('Parece que algúem não quer que você fuja')
                        time.sleep(0.5)
                        print('Você levou 5 de dano')
                        hp0=hp0 -5
                    else:
                        print('Você escapou com sucesso')
                        fugiu2=1
                        if fugiu2==1:
                            break
                elif decisao == 4:
                    print('Qual item você deseja usar?')
                    time.sleep(0.25)
                    inv=int(input('Inventário:\n    1-Poção - {}    2-Voltar'.format(pot)))
                    time.sleep(0.25)
                    if inv==1:
                        if pot>=1:
                            hp0=hp0+25
                            print('Você recuperou 25 de vida')
                        else:
                            print('Você não tem poções')
            if fugiu==2:
                time.sleep(0.25)
                print('Você ganhou 100 pontos!')
                pts=pts+100
            else:
                time.sleep(0.25)
                print('Você ganhou 200 pontos!')
                pts=pts+200
                if drop<15:
                    pot=pot+1
                    time.sleep(0.25)
                    print('Você encontra uma poção junto ao corpo do seu inimigo')
        if hp0<0:
            break
        if lago2=='S':
            print('Segurança em primeiro lugar!')
            time.sleep(0.25)

    print('Após sair de perto do lago, me deparo novamente com outra bifurcação. À esquerda estava a saída da masmorra, a qual me levaria a uma floresta.')
    time.sleep(2)
    print('Já a direita, havia trilhos e um carrinho de mina.')
    time.sleep(1)

    bif2=input('Qual caminho deseja seguir?\n1-Esquerda  2-Direita:\n->')
    if bif2=='1':
        print('Então cheguei na floresta. Os raios de luz mal passavam por entre as folhas.')
        time.sleep(1)
        print('Ao olhar no mapa, percebi que estava próximo de Gerudo Valley.')
        time.sleep(1)
        print('Mas antes que pudesse notar uma enorme aranha partiu para cima de mim!')
        trap3 = int(randint(0, 100))
        if trap3 < 30:
            hp_mob3 = 35
        elif trap3 > 75:
            hp_mob3 = 50
        else:
            hp_mob3 = 55
        time.sleep(0.5)
        while hp_mob3 > 0:
            if hp0 < 0:
                break
            print('Mob: {}  Você: {}'.format(hp_mob3, hp0))
            time.sleep(0.25)
            decisao = int(input('1-Atacar   2-Defender    3-Fugir     4-Item:\n-> '))
            time.sleep(0.25)
            if decisao == 1:
                combate = int(randint(1, 20))
                if combate < 10 and combate > 4:
                    hp_mob3 = hp_mob3 - 5
                    print('Você deu 5 de dano')
                    time.sleep(0.5)
                    print('O inimigo ataca de volta te dando {} de dano.'.format(ataque_mob3))
                    hp0 = hp0 - ataque_mob3
                elif combate < 3:
                    print('Errou!')
                    time.sleep(0.5)
                    print('O inimigo ataca de volta te dando {} de dano'.format(ataque_mob3))
                    hp0 = hp0 - ataque_mob3
                elif combate > 10 and combate < 18:
                    hp_mob3 = hp_mob3 - 10
                    print('Você deu 10 de dano')
                    time.sleep(0.5)
                    print('O inimigo ataca de volta te dando {} de dano'.format(ataque_mob3))
                    hp0 = hp0 - ataque_mob3
                else:
                    hp_mob3 = hp_mob3 - 20
                    print('Ataque crítico! 20 de dano')
                    time.sleep(0.5)
                    print('O inimigo ataca de volta te dando {} de dano'.format(ataque_mob3))
                    hp0 = hp0 - ataque_mob3
            elif decisao == 2:
                defesa = int(randint(1, 20))
                if defesa < 5:
                    hp0 = hp0 - 5
                    print('Sua defesa falhou')
                    time.sleep(0.5)
                    print('Você levou 5 de dano')
                else:
                    time.sleep(0.25)
                    print('Você bloqueou o ataque com sucesso!')
            elif decisao == 3:
                fuga = int(randint(1, 20))
                if fuga < 4:
                    print('Parece que algúem não quer que você fuja')
                    time.sleep(0.5)
                    print('Você levou 5 de dano')
                    hp0 = hp0 - 5
                else:
                    print('Você escapou com sucesso')
                    time.sleep(0.25)
                    fugiu3 = fugiu3 + 1
                    if fugiu3 == 1:
                        break
            elif decisao == 4:
                print('Qual item você deseja usar?')
                time.sleep(0.25)
                inv = int(input('Inventário:\n    1-Poção - {}    2-Voltar\n->'.format(pot)))
                if inv == 1:
                    if pot >= 1:
                        hp0 = hp0 + 25
                        time.sleep(0.25)
                        print('Você recuperou 25 de vida')
                    else:
                        time.sleep(0.25)
                        print('Você não tem poções')
        if fugiu3 == 1:
            time.sleep(0.5)
            print('Você ganhou 100 pontos!')
            pts = pts + 100
        else:
            time.sleep(0.5)
            print('Você ganhou 200 pontos!')
            pts = pts + 200
            if drop < 25:
                pot = pot + 1
                time.sleep(0.25)
                print('Você encontra uma poção junto ao cadáver')
        
print('Você perdeu')
print(nome,':',pts,'pontos')
