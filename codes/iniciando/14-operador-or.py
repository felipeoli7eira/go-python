

decisao = input('[E]ntrar | [S]air: ')

senha_digitada = input('Senha de entrada: ') or 'SS'
senha_de_entrada_definida = '123123'

if ((decisao == 'E' or decisao == 'e') and senha_digitada == senha_de_entrada_definida):
    print('Entrou...')
else:
    print('Saiu')
