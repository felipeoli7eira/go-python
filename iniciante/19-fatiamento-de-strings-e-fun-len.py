uma_string_qualquer = 'Uma string qualquer'


# fatiamento: [i:f:p]

# acessando um caracter da string pelo indice (varia de string para string)
print(uma_string_qualquer[2])
# acessando com indice negativo, a acontagem será da direita pra a esquerda
print(uma_string_qualquer[-4]) # q

# pegando de um ponto inicial ate um ponto final
print(uma_string_qualquer[4:10])

# para pegar ate o final, basta omitir o parametro final
print(uma_string_qualquer[0:])

# contando caracteres de uma string
print(len(uma_string_qualquer))

# alterando o passo
print(uma_string_qualquer[0:len(uma_string_qualquer):2])
print(uma_string_qualquer[::-1])