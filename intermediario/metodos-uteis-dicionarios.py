import copy

pessoa = {
    'nome': 'Felipe',
    'sobrenome': 'Oliveira',
    'enderecos': [
        {'rua': 'a', 'numero': 1}
    ]
}

print(len(pessoa))

print(pessoa.keys())
print(list(pessoa.keys()))
print(tuple(pessoa.keys()))
print(tuple(pessoa.items()))
print(tuple(pessoa.values()))

pessoa.setdefault('idade', 18)
print(pessoa['idade'])


print('-----------------------')
# pessoa_copy = pessoa.copy()
pessoa_copy = copy.deepcopy(pessoa)
print(pessoa_copy)

pessoa_copy['enderecos'][0]['rua'] = 'b'
print(pessoa_copy)
print(pessoa)

nome = pessoa.pop('nome')
print(nome)

ultima_chave = pessoa.popitem()
print(ultima_chave)

pessoa.update({
    'telefones': ['92345678'],
    'salario': 5000
})

pessoa.update(aniversario='16/11')

print(pessoa)

update_com_tupla = ("documento", "11122233344"),
pessoa.update(update_com_tupla)
print(pessoa)

update_com_lista = ("genero", "M"),
pessoa.update(update_com_lista)
print(pessoa)