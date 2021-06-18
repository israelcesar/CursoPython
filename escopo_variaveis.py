"""
Escopo de Variáveis

Dois casos de escopo:

1 - Variáveis globais;
    - Variáveis globais, são reconhecidas, ou seja, seu escopo compreende, todo o programa.

2 - Variáveis locais;
    - Variáveis locais, são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
    está limitado ao bloco onde foi declarada.

Para declarar variáveis em Python fazemos:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que
ao declararmos uma variável, nós não colocamos o tipo de dado dela.
Esse tipo é inferido ao atribuírmos o valor à mesma.

Exemplo em C:
int numero = 42

Exemplo em Java:
int numero = 42
"""

# Exemplo de variavel global
numero = 2
print(numero)

# A variáel novo é um exemplo de variável local, criada dentro do bloco do if
if numero > 10:
    novo = numero + 10
    print(novo)

