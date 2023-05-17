# sisteminha 1

entrada = input('Digite um numero inteiro: ')

if entrada.isdigit():
    entrada = int(entrada)

    if entrada % 2 == 0:
        print('PAR')
    else:
        print('IMPAR')
        print()
        print()
else:
    print('O numero nao parece ser um inteiro')

# sisteminha 2

entrada = input('Digite a hora atual (formato 24h): ')

try:
    entrada = int(entrada)
    if entrada >= 6 and entrada <= 11:
        print('Bom dia')
    elif entrada >= 12 and entrada <= 17:
        print('Boa tarde')
    elif entrada >= 18 and entrada <= 23:
        print('Boa noite')
    elif entrada >= 0 and entrada <= 5:
        print('Boa madrugada')
    else:
        print('Hora invalida')

    print()
    print()
except:
    print('Digite apenas numeros inteiros valido para hora')

# sisteminha 3

entrada = input('Digite seu primeiro nome: ')
tamanho_nome = len(entrada)
if entrada and tamanho_nome >= 3:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é médio')
    elif tamanho_nome >= 7:
        print('Seu nome é grande')
    else:
        print('Seu nome é muito grande')
else:
    print('Nenhum nome válido informado (min: 3 letras)')
