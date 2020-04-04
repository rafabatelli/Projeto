
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
        print('Agora você tem {0} fichas'.format(fichas))  
    elif 2<=soma1<=3 or soma1==12:
        fichas = fichas - aposta1
        print('Você perdeu.')
        print('Agora você tem {0} fichas'.format(fichas)) 
    else:
        def loop_point():
            soma2=sorteio()
            global fichas                   
            print('O seu valor point é o {0}'.format(soma1))
            print('O novo valor sorteado é',soma2)
            print('Você possui {0} fichas agora'.format(fichas))
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
def field():
    global aposta2
    global soma1
    global fichas
    print('A soma do resultado dos dados é',soma1)
    if 5<=soma1<=8:
        fichas = fichas - aposta2
        print('Você possui {0} fichas agora'.format(fichas))
    elif 3<=soma1<=4 or 9<=soma1<=11:
        fichas = fichas + aposta2
        print('Você possui {0} fichas agora'.format(fichas))
    elif soma1==2:
        fichas = fichas + 2*aposta2
        print('Você possui {0} fichas agora'.format(fichas))
    else:
        fichas = fichas + 3*aposta2
        print('Você possui {0} fichas agora'.format(fichas))

def any_craps():
    global aposta3
    global soma1
    global fichas
    print('A soma do resultado dos dados é',soma1)
    if soma1 == 2:
        fichas == fichas+(aposta3*7)
        print('Você possui {0} fichas agora'.format(fichas))    
    if soma1 == 3:
        fichas == fichas+(aposta3*7)
        print('Você possui {0} fichas agora'.format(fichas))   
    if soma1 == 12:
        fichas == fichas+(aposta3*7)
        print('Você possui {0} fichas agora'.format(fichas))  
    else:
        fichas = fichas - aposta3
        print('Você possui {0} fichas agora'.format(fichas))

def twelve():
    global aposta4
    global soma1
    global fichas
    print('A soma do resultado dos dados é',soma1)
    if soma1==12:
        fichas == fichas+(aposta4*30)
        print('Você possui {0} fichas agora'.format(fichas))
    else:
        fichas == fichas - aposta4
        print('Você possui {0} fichas agora'.format(fichas))
        




