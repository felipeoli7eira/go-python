nome = input('Digite seu nome: ')

try:
    if len(nome) < 3:
        print('Nome incorreto. Programa encerrado.')
        exit(0)
    else:
        contagem = 0
        nomeFruFru = ''
        while contagem < len(nome):
            nomeFruFru += f'*{nome[contagem]}'
            contagem += 1
        nomeFruFru += '*'
        print(nomeFruFru, end='')
except:
    print('Nome incorreto.')