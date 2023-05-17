nome = input('Digite seu nome: ')
idade = input('Digite seua idade: ')

if nome != '' and idade != '':
    print()
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    print(f'A primeira letra do seu nome é {nome[0]}')

    if ' ' in nome:
        print('Seu nome contém espaço')
    else:
        print('Seu nome não contém espaço')

    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print('Preencha todos os campos')