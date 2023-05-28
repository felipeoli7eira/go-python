letras = ['a', 'b', 'c', 'd']

a, b, c, d = letras
print(a, b, c, d)

outraListaQualquer = [1, 2, 3, 4, 5]
primeiroValor, *restoDosValores = outraListaQualquer
print(primeiroValor)
print(restoDosValores)

# ! por convencao, variaveis que nao serao usadas sao nomeadas com _ (underline):
foo = [1, 2, 3, 4, 5]
primeiroValorDaLista, *_ = foo


# Tuplas
# * Tuplas sao a mesma coisa que lista, a diferenca é que sao imutaveis

formaUmDeCriarTupla = 'Maria', 'Melica', 'Mel'
print(f'formaUmDeCriarTupla: {formaUmDeCriarTupla}')

formaDoisDeCriarTupla = ('Maria', 'Melica', 'Mel')
print(f'formaDoisDeCriarTupla: {formaDoisDeCriarTupla}') # da no mesmo

# conversoes
print('conversao de tupla para lista: ', list(formaDoisDeCriarTupla))
print('conversao de lista para tupla: ', tuple(formaDoisDeCriarTupla))


# ! Criando lista enumerada
lista = [1, 2, 3, 4, 5]

listaEnumerada = enumerate(lista)
print(listaEnumerada)
print(next(listaEnumerada))

for index, value in listaEnumerada:
    print(index, value)

print(list(listaEnumerada))