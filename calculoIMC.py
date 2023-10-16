peso = float(input('Qual o seu peso? '))
altura = float(input('Qual sua altura? '))
imc = peso / (altura ** 2)
if imc <= 18.4:
    print('Seu imc é: {:.2f} e você está abaixo do peso.'.format(imc))
elif imc <= 25:
    print('Seu imc é: {:.2f} e você está com o peso ideal.'.format(imc))
elif imc <= 30:
    print('Seu imc é: {:.2f} e você está com sobre peso'.format(imc))
elif imc <= 40:
    print('Seu imc é: {:.2f} e você está OBESO'.format(imc))
else:
    print('Seu imc é: {:.2f} e você com obesidade mórbida'.format(imc))