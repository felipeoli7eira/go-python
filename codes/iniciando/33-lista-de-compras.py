import os

lista = []

while True:
    
    try:
        opcao = input('Opcoes: [A]dicionar | [L]istar | [R]emover | [Z]erar: ').upper()

        if opcao == 'A':
            os.system('clear')
            produto = input('Produto: ')
            lista.append(produto)

        elif opcao == 'L':

            os.system('clear')
            print()

            if len(lista):
                for item in lista:
                    print(f'[{lista.index(item) + 1}]: {item}')
                print()
            else:
                print('Lista vazia')

        elif opcao == 'R':

            os.system('clear')

            print()
            for item in lista:
                print(f'[{lista.index(item) + 1}]: {item}')
            print()

            itemARemover = int(input('Qual item remover?: '))

            print(f'{lista[ itemARemover - 1 ]} removido(a)')
            del lista[ itemARemover - 1 ]

        elif opcao == 'Z':

            os.system('clear')
            lista.clear()
            print('Lista de compras zerada.')

        else:

            os.system('clear')
            print('Opcao invalida')
            continue
    except KeyboardInterrupt:
        os.system('clear')
        print('Sistena encerrado.')
        exit()
    except Exception:
        os.system('clear')
        print('Erro desconhecido!')
        exit(1)