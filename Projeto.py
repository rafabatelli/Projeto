
import random
fichas = 100
aposta1=0
aposta2=0
aposta3=0
aposta4=0

def apostar():
    if fichas > 0:
        pergunta1 = input('Você deseja apostar ou sair do jogo? (apostar/sair): ')
    if pergunta1 == 'sair'
        return False
    else:
        return True       
def sorteio():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    soma1 = dado1 + dado2
    return soma1
