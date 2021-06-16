"""
Recebendo dados do usuário
"""

# - Entrada de dados
nome = input('Qual o seu nome? - ').title()

# - Exemplo de print 'antigo' 2.x
# print('%s Qual sua idade?' % nome)

# - Exemplo de print 'novo' 3.x
# print('{0}, qual a sua idade?'.format(nome))

# - Exemplo de print 'mais atual' 3.7
idade = int(input(f'{nome.split()[0]}, qual a sua idade? - '))

# - Processamento

# - Saída de dados

# - Exemplo de print 'antigo' 2.x
# print('%s tem %s anos.' % (nome, idade))

# - Exemplo de print 'moderno' 3.x
# print('O(A) {0}, tem {1} anos.'.format(nome, idade))

# - Exemplo de print 'mais atual' 3.7
print(f'O(A) {nome}, nasceu em {2021 - idade} e tem {idade} anos.')
