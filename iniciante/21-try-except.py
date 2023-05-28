# Introdução
numero = input('Vou dobrar o numero que vc digitar: ')
try:
    numero = float(numero)
    dobro = numero * 2
    print(f'O dobro de {numero} e {dobro}')
except:
    print('Sistema encerrado.')