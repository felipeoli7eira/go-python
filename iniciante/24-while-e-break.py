condicao = True

while condicao:
    entrada = input('Digite seu nome: ')
    if entrada == 'Admin':
        condicao = False
        break
print('Programa encerrado.')