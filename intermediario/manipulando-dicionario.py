pessoa = {}

pessoa['primeiro_nome'] = 'Felipe'

chaveDinamica = 'sobrenome'
pessoa[chaveDinamica] = 'Oliveira'

pessoa['para_deletar'] = 'valor qualquer'
del pessoa['para_deletar']


if (pessoa.get('nao_existe') is not None):
    print(pessoa.get('nao_existe'))
else:
    print("Nao Existe")

print(pessoa)