"""
Tipo string

Em Phthon, um dado é considerado do tipo string sempre que:

- Estiver entre àspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre àspas duplas -> "uma string", "234", "a", "True", "42.3"
- Estiver entre àspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''
"""
# Estiver entre àspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.3"""

nome = 'Geek University'
# Transforma tudo em caixa alta
print(nome.upper())

# Transforma tudo em caixa baixa
print(nome.lower())

# Transformaem uma lista de strings
print(nome.split())

# [::-1] -> Começa do primeiro elemento, vai até o ultimo elemento e inverte
print(nome[::-1])
