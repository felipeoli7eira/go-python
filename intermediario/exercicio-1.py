perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opcoes': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opcoes': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opcoes': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0
for pergunta in perguntas:
    print('Pergunta: ', pergunta['Pergunta'])
    print()

    for indice, opcao in enumerate(pergunta['Opcoes']):
        print(f'{indice}) {opcao}')
    print()

    escolha = input('Escolha uma opção: ')
    acertou = False
    resposta_convert_int = None

    if escolha.isdigit():
        resposta_convert_int = int(escolha)

    if resposta_convert_int is not None:

        # verifico se escolheu uma opcao dentro do range de opcoes disponiveis
        if resposta_convert_int >= 0 and resposta_convert_int <= len(pergunta['Opcoes']):
            if pergunta['Opcoes'][resposta_convert_int] == pergunta['Resposta']:
                acertou = True

    print()

    if acertou:
        print('Acertou 👍')
        acertos += 1
    else:
        print('Errou 👎')

    print()

print()
print(f'Acertou {acertos} de {len(perguntas)}')
