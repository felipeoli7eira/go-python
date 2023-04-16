print(1, 2, 3, 4)
# por padrão o python separa os argumentos do print por espaço
print(10, 11, 12, 13, sep='-')


"""
argumento "end"

Com o argumento end da função print, é possível passar o que será inserido no final da linha do print, após o último
argumento. por padrão o python quebra a linha depois de exibir todos os argumentos, e isso tem uma especificidade
dependendo de cada SO (sistema operacional).
No windows é usado CRLF (\r\n)
Nos sistemas UNIX é usado LF (\n)
Mas o windows tem cada vez mais se aproximado das especificidades dos sistemas baseados em UNIX, fazendo com que
nas versões mais atuais de windows o LF (\n) seja compreendido e interpretado sem problemas.

Então com o argumento "end" é possível mudar o caracter final de linha, pode ser o que você quiser
"""

print('quebra de linha', end='\r\n')