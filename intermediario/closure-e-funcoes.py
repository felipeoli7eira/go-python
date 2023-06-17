"""
Closures e funções que retornam outras funções
"""

def multiplicador(numero):
    def exec(multiplicador):
        return numero * multiplicador
    return exec

por_dois   = multiplicador(2)
por_quatro = multiplicador(2)
por_seis   = multiplicador(2)

print(por_dois(2))
print(por_quatro(4))
print(por_seis(6))