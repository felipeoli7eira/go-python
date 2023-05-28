import os

palavraSecreta = 'programar'
letrasAcertadas = ''
tentativas = 0

while True:

    letraDigitada = input('Digite uma letra: ')

    if len(letraDigitada) > 1:
        print('\n!!! DIGITE APENAS UMA LETRA !!!\n')
        continue

    tentativas += 1

    if letraDigitada in palavraSecreta:
        letrasAcertadas += letraDigitada

    palavraFormadaComAsLetrasAcertadas = ''

    for letra in palavraSecreta:
        if letra in letrasAcertadas:
            palavraFormadaComAsLetrasAcertadas += letra
        else:
            palavraFormadaComAsLetrasAcertadas += '*'

    os.system('clear')
    print(f'\nResultado: {palavraFormadaComAsLetrasAcertadas}\n')
    
    if palavraFormadaComAsLetrasAcertadas == palavraSecreta:
        print('VOCE GANHOU!')
        print('TENTATIVAS: ', tentativas)
        letrasAcertadas = ''
        tentativas = 0
        palavraFormadaComAsLetrasAcertadas = ''