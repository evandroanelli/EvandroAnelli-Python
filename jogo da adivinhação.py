from random import randint
pc = randint(0,10)
print('-=-'*5)
print('Sou seu computador... Acabei de pensar em um número de 0 a 10.')
print('Consegue adivinhar?')
print('-=-'*5)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais... Tente de novo.')
        elif jogador > pc:
            print('Menos... Tente de novo>')
print('Acertou com {} tentativas. Parabéns!'.format(palpites))
print('-=-'*5)
