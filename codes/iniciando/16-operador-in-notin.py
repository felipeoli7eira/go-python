nomeDigitado = input('Digite seu nome: ')
needle = input('O que vc quer encontrar no nome?: ')

if (needle in nomeDigitado):
    print(f'{needle} esta em {nomeDigitado}')
else:
    print(f'{needle} nao esta em {nomeDigitado}')