# Lucas Quental e Samuel Kenji
from random import randint
import time

hp0 = 100
pot = 1
pot2 = 0
pts = 0
fugiu = 0
fugiu2 = 0
fugiu3 = 0
drop = randint(0, 100)

manual = ('Manual do jogo: \n'
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

print('Dia 14: Já faz 2 semanas que meu irmão Jeffrey está desaparecido. A última coisa que me lembro é ele dizendo que estava indo para Gerudo Valley...')
time.sleep(4)
print('Após o 3° dia do seu desaparecimento decidi ir em busca dele. Juntei minhas coisas e fui pela velha estrada de Victory Road.')
time.sleep(4)
print('A estrada era totalmente deserta, porém com árvores muito densas ao redor.')
time.sleep(4)
print('Em um determinado momento, caí em um buraco e machuquei minha perna, porém consegui escalar para fora do buraco e estava me recuperando, quando de repente...')
time.sleep(4.5)
print()

print("Desconhecido : Ei você! Precisa de ajuda? Meu nome é Papaco.")
time.sleep(2.5)
print("Papaco : Qual o seu nome?")
nome = input('->').title()
time.sleep(0.75)
print("Papaco : Olá", nome, ",parece que você procura por algo.")
time.sleep(2)
print("Papaco : Pelo jeito você é um forasteiro.")
time.sleep(2)
print("Papaco : Está aqui atrás de que?")
time.sleep(2.5)
print('->', nome, ": Estou atrás do meu irmão perdido.")
time.sleep(2)
print('->', nome, ": Ele sumiu faz alguns dias, mas antes disse que ia para a de Gerudo Valley...")
time.sleep(3)
print("Papaco : Talvez ele possa ter ido pelas masmorras, é o caminho mais rápido para lá.")
time.sleep(3)
print("Papaco : As masmorras ficam naquela direção. Apenas tenha cuidado em sua jornada.")
time.sleep(3)
print("Papaco : Existem várias criaturas que moram nas redondezas.")
time.sleep(2.5)
print("Papaco : Por segurança leve minha espada, meu escudo e minha poção.")
time.sleep(2.5)
print("Papaco : Faça bom uso desses equipamentos e boa sorte em sua jornada jovem", nome, ".")
time.sleep(2)
print()

bif = (input(
    'Então, eu entrei na masmorra e logo me deparo com uma bifurcação.\nDeseja ir para qual lado?\n1-Esquerda  2-Direita:\n->'))
time.sleep(0.25)

while hp0 > 0:
    if bif == 'esquerda' or bif == '1':
        mob_encounter = int(randint(0, 100))
        if mob_encounter < 35:
            hp_mob1 = 40
        elif mob_encounter > 75:
            hp_mob1 = 50
        else:
            hp_mob1 = 45
        print('Pouco tempo depois de entrar, um esqueleto se aproximou carregando uma espada enferrujada')
        time.sleep(0.5)
        while hp_mob1 > 0:
            if hp0 < 0:
                break
            print('Mob: {}  Você: {}'.format(hp_mob1, hp0))
            time.sleep(0.5)
            decisao = int(input('1-Atacar   2-Defender    3-Fugir     4-Item:\n-> '))
            time.sleep(0.5)
            ataque_mob = randint(4, 8)
            if decisao == 1:
                combate = int(randint(1, 20))
                if combate < 10 and combate > 4:
                    hp_mob1 = hp_mob1 - 5
                    print('Você deu 5 de dano')
                    time.sleep(0.5)
                    print('O inimigo ataca de volta te dando {} de dano.'.format(ataque_mob))
                    hp0 = hp0 - ataque_mob
                elif combate < 3:
                    print('Errou!')
                    time.sleep(0.5)
                    print('O inimigo ataca de volta te dando {} de dano'.format(ataque_mob))
                    hp0 = hp0 - ataque_mob
                elif combate > 10 and combate < 18:
                    hp_mob1 = hp_mob1 - 10
                    print('Você deu 10 de dano')
                    time.sleep(0.5)
                    print('O inimigo ataca de volta te dando {} de dano'.format(ataque_mob))
                    hp0 = hp0 - ataque_mob
                else:
                    hp_mob1 = hp_mob1 - 20
                    print('Ataque crítico! 20 de dano')
                    time.sleep(0.5)
                    print('O inimigo ataca de volta te dando {} de dano'.format(ataque_mob))
                    hp0 = hp0 - ataque_mob
            elif decisao == 2:
                defesa = int(randint(1, 20))
                if defesa < 5:
                    hp0 = hp0 - 5
                    print('Sua defesa falhou')
                    time.sleep(0.5)
                    print('Você levou 5 de dano')
                else:
                    time.sleep(0.5)
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
                    time.sleep(0.5)
                    fugiu = fugiu + 1
                    if fugiu == 1:
                        break
            elif decisao == 4:
                print('Qual item você deseja usar?')
                time.sleep(0.5)
                inv = int(input('Inventário:\n    1-Poção (25hp) - {}    2-Voltar\n->'.format(pot)))
                if inv == 1:
                    if pot >= 1:
                        hp0 = hp0 + 25
                        time.sleep(0.5)
                        print('Você recuperou 25 de vida')
                        pot=pot-1
                    else:
                        time.sleep(0.5)
                        print('Você não tem poções')
        if fugiu == 1:
            time.sleep(0.5)
            print('Você ganhou 100 pontos!')
            pts = pts + 100
        else:
            time.sleep(0.5)
            print('Você ganhou 200 pontos!')
            pts = pts + 200
            if drop < 25:
                pot = pot + 1
                time.sleep(0.5)
                print('Você encontra uma poção junto ao cadáver')
    if bif == 'direita' or bif == '2':
        bau = int(randint(0, 50))
        if bau < 20:
            bau_abrir = input('Você encontrou um baú. Deseja abri-lo? (S/N)\n-> ').upper()
            if bau_abrir == 'S':
                trap = int(randint(0, 100))
                if trap < 15:
                    time.sleep(0.5)
                    print('Era uma armadilha!')
                    time.sleep(0.5)
                    print('Você levou 5 de dano')
                    hp0 = hp0 - 5
                    if hp0 < 0:
                        break
                elif trap > 15 and trap < 100:
                    time.sleep(0.5)
                    print('Você achou uma poção!')
                    pot = pot + 1
                else:
                    time.sleep(0.5)
                    print('Você achou duas poções!')
                    pot = pot + 2
            elif bau_abrir == 'N':
                time.sleep(0.5)
                print('Melhor prevenir do que remediar, não é mesmo?')
    if hp0 < 0:
        break
    time.sleep(0.5)
    print('Mais ao fim da primeira grande seção me deparo com um grande lago')
    time.sleep(0.5)
    lago = input(
        'Ao olhar mais de perto percebo que há um brilho misterioso vindo do fundo dele\nDeseja investigar? (S/N)\n->').upper()
    if lago == "S":
        trap2 = int(randint(0, 100))
        if trap2 < 30:
            hp_mob2 = 35
        elif trap2 > 75:
            hp_mob2 = 50
        else:
            hp_mob2 = 55
        time.sleep(0.5)
        print('Era o brilho de um monstro aquático!')
        time.sleep(0.5)
        while hp_mob2 > 0:
            if hp0 < 0:
                break
            ataque_mob2 = randint(5, 9)
            print('Mob: {}  Você: {}'.format(hp_mob2, hp0))
            time.sleep(0.5)
            decisao = int(input('1-Atacar   2-Defender    3-Fugir     4-Item:\n-> '))
            time.sleep(0.5)
            if decisao == 1:
                combate = int(randint(1, 20))
                if combate < 10 and combate > 4:
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
                    hp0 = hp0 - 5
                else:
                    print('Você escapou com sucesso')
                    fugiu2 = 1
                    if fugiu2 == 1:
                        break
            elif decisao == 4:
                print('Qual item você deseja usar?')
                time.sleep(0.5)
                inv = int(input('Inventário:\n    1-Poção (25hp) - {}    2-Voltar\n->'.format(pot)))
                if inv == 1:
                    if pot >= 1:
                        hp0 = hp0 + 25
                        time.sleep(0.5)
                        print('Você recuperou 25 de vida')
                        pot=pot-1
                    else:
                        time.sleep(0.5)
                        print('Você não tem poções')
        if fugiu2 == 1:
            time.sleep(0.5)
            print('Você ganhou 100 pontos!')
            pts = pts + 100
        else:
            time.sleep(0.5)
            print('Você ganhou 200 pontos!')
            pts = pts + 200
            if drop < 15:
                time.sleep(0.5)
                print('Você achou uma poção junto ao cadáver')
                pot = pot + 1
    else:
        time.sleep(0.5)
        lago2 = (input('Um barulho muito estranho emana do lago. Deseja ignorá-lo mesmo assim? (S/N)\n->')).upper()
        if lago2 == 'N':
            trap2 = int(randint(0, 100))
            if trap2 < 30:
                hp_mob2 = 35
            elif trap2 > 75:
                hp_mob2 = 50
            else:
                hp_mob2 = 55
            time.sleep(0.5)
            print('Um monstro emergiu do lago!')
            time.sleep(0.5)
            while hp_mob2 > 0:
                if hp0 < 0:
                    break
                print('Mob: {}  Você: {}'.format(hp_mob2, hp0))
                ataque_mob = randint(5, 9)
                time.sleep(0.5)
                decisao = int(input('1-Atacar   2-Defender    3-Fugir     4-Item:\n->'))
                time.sleep(0.5)
                if decisao == 1:
                    combate = int(randint(1, 20))
                    if combate < 10 and combate > 4:
                        hp_mob2 = hp_mob2 - 5
                        print('Você deu 5 de dano')
                        time.sleep(0.5)
                        print('O inimigo ataca de volta te dando {} de dano.'.format(ataque_mob))
                        hp0 = hp0 - ataque_mob
                    elif combate < 3:
                        print('Errou!')
                        time.sleep(0.5)
                        print('O inimigo ataca de volta te dando {} de dano'.format(ataque_mob))
                        hp0 = hp0 - ataque_mob
                    elif combate > 10 and combate < 18:
                        hp_mob2 = hp_mob2 - 10
                        print('Você deu 10 de dano')
                        time.sleep(0.5)
                        print('O inimigo ataca de volta te dando {} de dano'.format(ataque_mob))
                        hp0 = hp0 - ataque_mob
                    else:
                        hp_mob2 = hp_mob2 - 20
                        print('Ataque crítico! 20 de dano')
                        time.sleep(0.5)
                        print('O inimigo ataca de volta te dando {} de dano'.format(ataque_mob))
                        hp0 = hp0 - ataque_mob
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
                        hp0 = hp0 - 5
                    else:
                        print('Você escapou com sucesso')
                        fugiu2 = 1
                        if fugiu2 == 1:
                            break
                elif decisao == 4:
                    print('Qual item você deseja usar?')
                    time.sleep(0.5)
                    inv = int(input('Inventário:\n    1-Poção (25hp) - {}    2-Voltar'.format(pot)))
                    time.sleep(0.5)
                    if inv == 1:
                        if pot >= 1:
                            hp0 = hp0 + 25
                            print('Você recuperou 25 de vida')
                            pot=pot-1
                        else:
                            print('Você não tem poções')
            if fugiu2 == 1:
                time.sleep(0.5)
                print('Você ganhou 100 pontos!')
                pts = pts + 100
            else:
                time.sleep(0.5)
                print('Você ganhou 200 pontos!')
                pts = pts + 200
                if drop < 15:
                    pot2 = pot2 + 1
                    time.sleep(0.5)
                    print('Você encontrou uma poção grande!')
        if hp0 < 0:
            break
        if lago2 == 'S':
            print('Segurança em primeiro lugar!')
            time.sleep(0.5)

    print('Após sair de perto do lago, me deparo novamente com uma bifurcação. À esquerda estava a saída da masmorra, a qual me levaria a uma floresta.')
    time.sleep(2)
    print('Já a direita, havia trilhos e um carrinho de mina.')
    time.sleep(1)

    bif2 = input('Qual caminho deseja seguir?\n1-Esquerda  2-Direita:\n->')
    if bif2 == '1':
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
            hp_mob3 = 45
        time.sleep(0.5)
        while hp_mob3 > 0:
            if hp0 < 0:
                break
            print('Mob: {}  Você: {}'.format(hp_mob3, hp0))
            time.sleep(0.5)
            ataque_mob3=randint(3,10)
            decisao = int(input('1-Atacar   2-Defender    3-Fugir     4-Item:\n-> '))
            time.sleep(0.5)
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
                    time.sleep(0.5)
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
                    time.sleep(0.5)
                    fugiu3 = fugiu3 + 1
                    if fugiu3 == 1:
                        break
            elif decisao == 4:
                print('Qual item você deseja usar?')
                time.sleep(0.5)
                inv = int(input('Inventário:\n    1-Poção (25hp) - {}  2-Poção Grande (50hp) - {}  3-Voltar\n->'.format(pot,pot2)))
                if inv == 1:
                    if pot >= 1:
                        hp0 = hp0 + 25
                        time.sleep(0.5)
                        print('Você recuperou 25 de vida')
                        pot=pot-1
                    else:
                        time.sleep(0.5)
                        print('Você não tem poções')
                if inv == 2:
                    if pot2>= 1:
                        hp0=hp0+50
                        time.sleep(0.5)
                        print('Você recuperou 50 de vida')
                        pot2=pot2-1
                    else:
                        time.sleep(0.5)
                        print('Você não tem poções')
        if fugiu3 == 1:
            time.sleep(0.5)
            print('Você ganhou 100 pontos!')
            pts = pts + 100
        else:
            time.sleep(0.5)
            print('Você ganhou 200 pontos!')
            pts = pts + 200
            pot2 = pot2 + 2
            time.sleep(0.5)
            print('Você encontra duas poções grandes!')

    if bif2=='2':
        print('Eu resolvi seguir em direção à mina. "Pelo jeito está abandonada a muito tempo", eu pensei.')
        time.sleep(3)
        print('Olhando ao redor, vi que tinham muitas ferramentas, mas todas enferrujadas e cobertas de teias.')
        time.sleep(4)
        print('Andei mais um pouco e me deparei com 2 caminhos mais uma vez, pórem um dos caminhos estava completamente barrado.')
        time.sleep(4)
        print('"Provavelmente ele levava para mais fundo da mina".')
        time.sleep(3)
        print('Então segui no caminho que estava livre e achei uma das saídas da masmorra.')
        time.sleep(3)
        print('Mas, pra variar, um Troll aparece no meu caminho.')
        time.sleep(2.5)

        trap4 = int(randint(0, 100))
        if trap4 < 30:
            hp_mob4 = 35
        elif trap4 > 75:
            hp_mob4 = 50
        else:
            hp_mob4 = 45
        time.sleep(0.5)
        while hp_mob4 > 0:
            if hp0 < 0:
                break
            print('Mob: {}  Você: {}'.format(hp_mob4, hp0))
            time.sleep(0.5)
            ataque_mob4=randint(3,10)
            decisao = int(input('1-Atacar   2-Defender    3-Fugir     4-Item:\n-> '))
            time.sleep(0.5)
            if decisao == 1:
                combate = int(randint(1, 20))
                if combate < 10 and combate > 4:
                    hp_mob4 = hp_mob4 - 5
                    print('Você deu 5 de dano')
                    time.sleep(0.5)
                    print('O inimigo ataca de volta te dando {} de dano.'.format(ataque_mob4))
                    hp0 = hp0 - ataque_mob4
                elif combate < 3:
                    print('Errou!')
                    time.sleep(0.5)
                    print('O inimigo ataca de volta te dando {} de dano'.format(ataque_mob4))
                    hp0 = hp0 - ataque_mob4
                elif combate > 10 and combate < 18:
                    hp_mob4 = hp_mob4 - 10
                    print('Você deu 10 de dano')
                    time.sleep(0.5)
                    print('O inimigo ataca de volta te dando {} de dano'.format(ataque_mob4))
                    hp0 = hp0 - ataque_mob4
                else:
                    hp_mob4 = hp_mob4 - 20
                    print('Ataque crítico! 20 de dano')
                    time.sleep(0.5)
                    print('O inimigo ataca de volta te dando {} de dano'.format(ataque_mob4))
                    hp0 = hp0 - ataque_mob4
            elif decisao == 2:
                defesa = int(randint(1, 20))
                if defesa < 5:
                    hp0 = hp0 - 5
                    print('Sua defesa falhou')
                    time.sleep(0.5)
                    print('Você levou 5 de dano')
                else:
                    time.sleep(0.5)
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
                    time.sleep(0.5)
                    fugiu3 = fugiu3 + 1
                    if fugiu3 == 1:
                        break
            elif decisao == 4:
                print('Qual item você deseja usar?')
                time.sleep(0.5)
                inv = int(input('Inventário:\n    1-Poção (25hp) - {}  2-Poção Grande (50hp) - {}  3-Voltar\n->'.format(pot,pot2)))
                if inv == 1:
                    if pot >= 1:
                        hp0 = hp0 + 25
                        time.sleep(0.5)
                        print('Você recuperou 25 de vida')
                        pot=pot-1
                    else:
                        time.sleep(0.5)
                        print('Você não tem poções')
                if inv == 2:
                    if pot2>= 1:
                        hp0=hp0+50
                        time.sleep(0.5)
                        print('Você recuperou 50 de vida')
                        pot2=pot2-1
                    else:
                        time.sleep(0.5)
                        print('Você não tem poções')
        if fugiu3 == 1:
            time.sleep(0.5)
            print('Você ganhou 100 pontos!')
            pts = pts + 100
        else:
            time.sleep(0.5)
            print('Você ganhou 200 pontos!')
            pts = pts + 200
            pot2 = pot2 + 2
            time.sleep(0.5)
            print('Você encontra duas poções grandes!')


    print('Após a luta, percebo que cheguei em Gerudo Valley. Ao caminhar um pouco pela região, vejo uma casa bem velha e escondida por entre os galhos e folhas.')
    time.sleep(4)
    print('Passando ao redor da casa ouço risadas maléficas e alguém chorando lá dentro.')
    time.sleep(3.5)
    print('Ao parar para ouvir melhor, percebo que a voz de quem estava chorando era a do meu irmão! "Ele deve ter sido sequestrado!"')
    time.sleep(3.5)
    print('Logo que me toquei, invadi a casa dando um chute na porta e gritei:')
    time.sleep(3.5)
    print('SOLTEM O JEFFREY!!!')
    time.sleep(2)
    print('Dois dos sequestradores olharam para o que parecia ser o chefe, que disse: Peguem esse cara também!')
    time.sleep(3)
    print('Várias frases de efeito passaram pela minha cabeça, mas não era hora para brincadeiras...')
    time.sleep(3)

    trap5 = int(randint(0, 100))
    if trap5 < 30:
        hp_mob5 = 35
    elif trap5 > 75:
        hp_mob5 = 50
    else:
        hp_mob5 = 45
    time.sleep(0.5)
    while hp_mob5 > 0:
        if hp0 < 0:
            break
        print('Mob: {}  Você: {}'.format(hp_mob5, hp0))
        time.sleep(0.5)
        ataque_mob5 = randint(5, 10)
        decisao = int(input('1-Atacar   2-Defender    3-Fugir     4-Item:\n-> '))
        time.sleep(0.5)
        if decisao == 1:
            combate = int(randint(1, 20))
            if combate < 10 and combate > 4:
                hp_mob5 = hp_mob5 - 5
                print('Você deu 5 de dano')
                time.sleep(0.5)
                print('O inimigo ataca de volta te dando {} de dano.'.format(ataque_mob5))
                hp0 = hp0 - ataque_mob5
            elif combate < 3:
                print('Errou!')
                time.sleep(0.5)
                print('O inimigo ataca de volta te dando {} de dano'.format(ataque_mob5))
                hp0 = hp0 - ataque_mob5
            elif combate > 10 and combate < 18:
                hp_mob5 = hp_mob5 - 10
                print('Você deu 10 de dano')
                time.sleep(0.5)
                print('O inimigo ataca de volta te dando {} de dano'.format(ataque_mob5))
                hp0 = hp0 - ataque_mob5
            else:
                hp_mob5 = hp_mob5 - 20
                print('Ataque crítico! 20 de dano')
                time.sleep(0.5)
                print('O inimigo ataca de volta te dando {} de dano'.format(ataque_mob5))
                hp0 = hp0 - ataque_mob5
        elif decisao == 2:
            defesa = int(randint(1, 20))
            if defesa < 5:
                hp0 = hp0 - 5
                print('Sua defesa falhou')
                time.sleep(0.5)
                print('Você levou 5 de dano')
            else:
                time.sleep(0.5)
                print('Você bloqueou o ataque com sucesso!')
        elif decisao == 3:
            print('Seu irmão está em grave perigo. Melhor não fazer isso.')
        elif decisao == 4:
            print('Qual item você deseja usar?')
            time.sleep(0.5)
            inv = int(input(
                'Inventário:\n    1-Poção (25hp) - {}  2-Poção Grande (50hp) - {}  3-Voltar\n->'.format(pot, pot2)))
            if inv == 1:
                if pot >= 1:
                    hp0 = hp0 + 25
                    time.sleep(0.5)
                    print('Você recuperou 25 de vida')
                    pot = pot - 1
                else:
                    time.sleep(0.5)
                    print('Você não tem poções')
            if inv == 2:
                if pot2 >= 1:
                    hp0 = hp0 + 50
                    time.sleep(0.5)
                    print('Você recuperou 50 de vida')
                    pot2 = pot2 - 1
                else:
                    time.sleep(0.5)
                    print('Você não tem poções')
    time.sleep(0.5)
    print('Você ganhou 200 pontos!')
    pts = pts + 200
    pot2 = pot2 + 1
    time.sleep(0.5)
    print('Você encontra uma poção grande!')
    time.sleep(1)

    print('Um já foi, faltam dois.')
    time.sleep(1)

    trap5 = int(randint(0, 100))
    if trap5 < 30:
        hp_mob6 = 35
    elif trap5 > 75:
        hp_mob6 = 50
    else:
        hp_mob6 = 45
    time.sleep(0.5)
    while hp_mob6 > 0:
        if hp0 < 0:
            break
        print('Mob: {}  Você: {}'.format(hp_mob6, hp0))
        time.sleep(0.5)
        ataque_mob6 = randint(5, 10)
        decisao = int(input('1-Atacar   2-Defender    3-Fugir     4-Item:\n-> '))
        time.sleep(0.5)
        if decisao == 1:
            combate = int(randint(1, 20))
            if combate < 10 and combate > 4:
                hp_mob6 = hp_mob6 - 5
                print('Você deu 5 de dano')
                time.sleep(0.5)
                print('O inimigo ataca de volta te dando {} de dano.'.format(ataque_mob6))
                hp0 = hp0 - ataque_mob6
            elif combate < 3:
                print('Errou!')
                time.sleep(0.5)
                print('O inimigo ataca de volta te dando {} de dano'.format(ataque_mob6))
                hp0 = hp0 - ataque_mob6
            elif combate > 10 and combate < 18:
                hp_mob6 = hp_mob6 - 10
                print('Você deu 10 de dano')
                time.sleep(0.5)
                print('O inimigo ataca de volta te dando {} de dano'.format(ataque_mob6))
                hp0 = hp0 - ataque_mob6
            else:
                hp_mob6 = hp_mob6 - 20
                print('Ataque crítico! 20 de dano')
                time.sleep(0.5)
                print('O inimigo ataca de volta te dando {} de dano'.format(ataque_mob6))
                hp0 = hp0 - ataque_mob6
        elif decisao == 2:
            defesa = int(randint(1, 20))
            if defesa < 5:
                hp0 = hp0 - 5
                print('Sua defesa falhou')
                time.sleep(0.5)
                print('Você levou 5 de dano')
            else:
                time.sleep(0.5)
                print('Você bloqueou o ataque com sucesso!')
        elif decisao == 3:
            print('Seu irmão está em grave perigo. Melhor não fazer isso.')
        elif decisao == 4:
            print('Qual item você deseja usar?')
            time.sleep(0.5)
            inv = int(input(
                'Inventário:\n    1-Poção (25hp) - {}  2-Poção Grande (50hp) - {}  3-Voltar\n->'.format(pot, pot2)))
            if inv == 1:
                if pot >= 1:
                    hp0 = hp0 + 25
                    time.sleep(0.5)
                    print('Você recuperou 25 de vida')
                    pot = pot - 1
                else:
                    time.sleep(0.5)
                    print('Você não tem poções')
            if inv == 2:
                if pot2 >= 1:
                    hp0 = hp0 + 50
                    time.sleep(0.5)
                    print('Você recuperou 50 de vida')
                    pot2 = pot2 - 1
                else:
                    time.sleep(0.5)
                    print('Você não tem poções')
    time.sleep(0.5)
    print('Você ganhou 200 pontos!')
    pts = pts + 200
    pot2 = pot2 + 1
    time.sleep(0.5)
    print('Você encontra uma poção grande!')
    time.sleep(1)

    print('Sequestrador: Você pode até ter derrotado meus capangas, mas a verdadeira batalha começa agora!')
    time.sleep(1)

    time.sleep(0.5)
    hp_boss = 200
    while hp_boss > 0:
        if hp0 < 0:
            break
        print('Boss: {}  Você: {}'.format(hp_boss, hp0))
        time.sleep(0.5)
        ataque_boss = randint(5, 20)
        decisao = int(input('1-Atacar   2-Defender    3-Fugir     4-Item:\n-> '))
        time.sleep(0.5)
        if decisao == 1:
            combate = int(randint(1, 20))
            if combate < 10 and combate > 4:
                hp_boss = hp_boss - 5
                print('Você deu 5 de dano')
                time.sleep(0.5)
                print('O inimigo ataca de volta te dando {} de dano.'.format(ataque_boss))
                hp0 = hp0 - ataque_boss
            elif combate < 3:
                print('Errou!')
                time.sleep(0.5)
                print('O inimigo ataca de volta te dando {} de dano'.format(ataque_boss))
                hp0 = hp0 - ataque_boss
            elif combate > 10 and combate < 18:
                hp_boss = hp_boss - 10
                print('Você deu 10 de dano')
                time.sleep(0.5)
                print('O inimigo ataca de volta te dando {} de dano'.format(ataque_boss))
                hp0 = hp0 - ataque_boss
            else:
                hp_boss = hp_boss - 20
                print('Ataque crítico! 20 de dano')
                time.sleep(0.5)
                print('O inimigo ataca de volta te dando {} de dano'.format(ataque_boss))
                hp0 = hp0 - ataque_boss
        elif decisao == 2:
            defesa = int(randint(1, 20))
            if defesa < 5:
                hp0 = hp0 - 5
                print('Sua defesa falhou')
                time.sleep(0.5)
                print('Você levou 5 de dano')
            else:
                time.sleep(0.5)
                print('Você bloqueou o ataque com sucesso!')
        elif decisao == 3:
            print('Seu irmão está em grave perigo. Melhor não fazer isso.')
        elif decisao == 4:
            print('Qual item você deseja usar?')
            time.sleep(0.5)
            inv = int(input(
                'Inventário:\n    1-Poção (25hp) - {}  2-Poção Grande (50hp) - {}  3-Voltar\n->'.format(pot, pot2)))
            if inv == 1:
                if pot >= 1:
                    hp0 = hp0 + 25
                    time.sleep(0.5)
                    print('Você recuperou 25 de vida')
                    pot = pot - 1
                else:
                    time.sleep(0.5)
                    print('Você não tem poções')
            if inv == 2:
                if pot2 >= 1:
                    hp0 = hp0 + 50
                    time.sleep(0.5)
                    print('Você recuperou 50 de vida')
                    pot2 = pot2 - 1
                else:
                    time.sleep(0.5)
                    print('Você não tem poções')
    time.sleep(0.5)
    print('Você ganhou 1000 pontos!')
    pts = pts + 1000


print('Você perdeu')
print(nome, ':', pts, 'pontos')
