string = 'Felipe Oliveira'
lista = ['Felipe', 'Alves', 'de', 'Oliveira']
tupla = 'Felipe', 'Alves', 'de', 'Oliveira'

primeiroNome, Sobrenome, *resto = lista

print(Sobrenome)

for nomes in lista:
    print(nomes, end=' ')

print(*lista)
print(*tupla)
print(*string)