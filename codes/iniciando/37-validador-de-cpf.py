# CPF gerado na internet: 754.316.675-56

# Coletar a soma dos 9 primeiros digitos do CPF, multiplicando cada um dos valores por uma contagem
#  regressiva comecando de 10

# ---> EX:
# Nove primeiros digitos:                                    7   5  4  3  1  6  6  7  5
# x:                                                         x   x  x  x  x  x  x  x  x
# Contagem regressiva:                                       10  9  8  7  6  5  4  3  2

# Resultado do digito multiplicado pelo numero da contagem:  70  45 32 21 6  30 24 21 10
# Soma dos valores resultados da multiplicacao:              259
# Multiplicar o resultado anterior por 10:                   2.590
# Pegar o resto da divisao do numero anterior por 11:        5
# Se o resultado do resto da divisao for maior que 9, assumir 0 (zero) como resultado final da conta
# Se nao, assumir o proprio valor

# No caso desse CPF de exemplo, o resultado final deu 5, que bate com o primeiro digito dele

doc = '75431667556'
contagem = 10 # 11 para q a contagem leve em consideracao o 10

dig_x_contagem_res = 0

nove_primeiros_digitos = doc[0:9]
for digito in nove_primeiros_digitos:
    dig_x_contagem_res += int(digito) * contagem
    contagem -= 1

resto_da_divisao = (dig_x_contagem_res * 10) % 11

primeiro_digito_verificador = resto_da_divisao if resto_da_divisao < 9 else 0

print(primeiro_digito_verificador)


# o calculo do segundo digito fiquei com preguica de fazer...