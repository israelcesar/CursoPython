"""
Ranges

- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequências numéricas, não de forma aleatória,
mas sim de maneira especificada.

Formas gerais:

# Forma 1

range(valor_de_parada)
OBS: valor_de_parada não inclusive (início padrão 0, passo de 1 em 1)

# Exemplo Forma 1
for num in range(11):
    print(num)


# Forma 2

range(valor_de_inicio, valor_de_parada)
OBS: valor_de_parada não inclusive (início especificado, passo de 1 em 1)

# Exemplo Forma 2
for num in range(1,11):
    print(num)


# Forma 3

range(valor_de_inicio, valor_de_parada, passo)
OBS: valor_de_parada não inclusive (passo especificado pelo usuário)

# Exemplo Forma 3
for num in range(5, 50, 5):
    print(num)


# Forma 4 (igual Forma 3 sendo inversa)

range(valor_de_inicio, valor_de_parada, passo)
OBS: valor_de_parada não inclusive (inicio especificado pelo usuário e passo especificado pelo usuário)

# Exemplo Forma 4
for num in range(10, 0, -1):
    print(num)
"""
