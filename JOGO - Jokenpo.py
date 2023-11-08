import random
import time
opcoes = ['Pedra', 'Papel', 'Tesoura']
print('-=-'* 11)
print('JOKENPÔ - Escolha: Pedra, Papel ou Tesoura!')
print('-=-'* 11)
x1 = input('Eu escolho: ')
pc = random.choice(opcoes)
print('PC ESCOLHE: {}'.format(pc))
print('-=-'* 11)
print('Calculando...')
time.sleep(1)
print('-=-'* 11)
if x1 in opcoes:
    if x1 == pc:
        print('Empate!')
    elif (x1 == 'Pedra' and pc == 'Tesoura') or (x1 == 'Papel' and pc == 'Pedra') or (x1 == 'Tesoura' and pc == 'Papel'):
        print('Você venceu!')
    else:
        print('PC venceu!')
else:
    print('Escolha inválida. Por favor, escolha entre Pedra, Papel ou Tesoura.')
print('-=-'* 11)