nome = 'Felipe'
altura = 1.65
peso = 67.00

mensagem = f'{nome} tem {altura:.2f}m de altura e peso de {peso:.2f}kg'
print(mensagem)

# f-strings (formatação)

# formatação com a função format

a = 'a'
b = 'b'
c = 'c'

print('a: {} | b: {} | c: {}'.format(a, b, c))
print('a: {var_a} | b: {var_a} | c: {var_a}'.format(var_a=a, var_b=b, var_c=c))