lista = [11, 12, 13, 14, 15]
print('como a lista comecou: ', lista)

del lista[0]
print('lista apos o del lista[1]: ', lista)

lista.pop()
print('lista apos o .pop(): ', lista)

lista.append(100)
print('lista apos o .append(100): ', lista)

print('acessando um indice de forma negativa: ', lista[-1])

del lista[-1]
print('Deletando um indice usando del lista[-1]: ', lista)

lista.insert(0, 10)
print('inserindo um valor em um indice: ', lista)

lista.clear()
print('Limpando lista com .clear(): ', lista)


lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

lista_c = lista_a + lista_b
print('lista c: ', lista_c)

lista_d = lista_b.extend([7, 8, 9])
print('lista d: ', lista_d) # None
print(lista_b)


garotas = ['Maria', 'Julia', 'Helena']
garotas.append('Gabriela')
for garota in garotas:
    print(f'{garota}: ', garotas.index(garota))