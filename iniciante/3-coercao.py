# Coerção de dados nada mais é do que converção, ou seja, transformar um dado de um tipo para
# outro tipo

"""
Coerção tbm tem outros nomes:

Conversão
type convertion
typecasting
coercion
"""

print(int('21'))
print(type(int('21'))) # <class 'int'>
print(int('21') + 4) # 25
print(float('1') + 1) # 2.0
print(bool('')) # False
print(bool(' ')) # True
print(type(str(11))) # <class 'str'>
print(str(11) + 'abc') # 11abc