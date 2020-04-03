
import random
fichas = 100
aposta1=0
aposta2=0
aposta3=0
aposta4=0
soma1=0
def apostar():
    pergunta1 = input('Você deseja apostar ou sair do jogo? (apostar/sair): ')
    if pergunta1 == 'apostar':
        return True
    else:
        return False
          
def sorteio():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    valor = dado1 + dado2
    return valor
def pass_line_bet():
    global aposta1
    global soma1
    global fichas
    
    print('A soma do resultado dos dados é',soma1)        
    if soma1==7 or soma1==11:
        fichas = fichas + aposta1
        print('Você ganhou.')
        print('Agora você tem',fichas)  
    elif 2<=soma1<=3 or soma1==12:
        fichas = fichas - aposta1
        print('Você perdeu.')
        print('Agora você tem',fichas)
    else:
        def loop_point():
            soma2=sorteio()
            global fichas                   
            print('O seu valor point é o {0}'.format(soma1))
            print('O novo valor sorteado é',soma2)
            print('Agora você tem',fichas) 
            if(soma2==soma1):
                fichas=fichas+aposta1
                print('Você sorteu o seu valor point')
                return True
            elif(soma2==7):
                fichas=fichas-aposta1
                print("você perdeu tudo!!!")
                return True
            else:
                return False
        while(loop_point()!=True):
            loop_point()
  

def apostas():
    while True:
        global soma1
        soma1=sorteio()
        pergunta2 = input('Você deseja apostar em Pass Line Bet? (sim/não):')
        if pergunta2 == 'sim':
            aposta1 = int(input('quanto vc deseja apostar?'))
            pass_line_bet()

if (apostar()==True):
    while(fichas>0):
        apostas()
else:
    print("Obrigado por jogar") 