'''SOBRE O PYTHON
    * Linguagem de programação de alto nível, propósito geral, interpretada, imperativa, orientada a objetos,
        funcional, com tipagem forte e dinâmica;
    * Criada por Guido van Rossum em 1991;
    * Modelo de desenvolvimento open-source;
    * Gerenciada pela organização sem fins lucrativos Python Software Foundation;
    * Altamente utilizada para scripts, machine learning, processamento de imagens, web, computação científica,
        dentre outros;
    * Usada na Wikipedia, Google, Yahoo!, NASA, Facebook, Amazon, Instagram, Spotify, Reddit etc.

    A filosofia do Python é enfatizar a importância do esforço do programador sobre o esforço computacional, dando
    ênfase à legibilidade do código sobre a velocidade.

    Foi criada com base na linguagem ABC, possuindo sintaxe influencidada pelo C, além de compreensão de listas,
    funções anônimas e função map inspiradas do Haskell. Os iteradores são baseados na Icon, tratamento de exceção
    e módulos da Modula-3 e expressões regulares de Perl.'''

#   -----> Declarando váriaveis em python <-----

#inteiros:
idade = 21

#float:
altura = 1.71

#Strings:
nome = 'Fulano de Tal'

#Booleanos:
gosta_de_Python = True



#   -----> Funções Úteis <-----
'''
input("mensagem opcional de entrada: ") #lê no terminal
print(valor) #escreve no terminal
int(minha_string) #transforma a string em inteiro
float(minha_String) #transforma a string em ponto flutuante  '''

#printando valores:
print(idade)
print(altura)
print(nome)
print(gosta_de_Python)

#lendo valores:
meu_nome = input("digite seu nome: ")

# '+' concatena duas strings:
print('olá ' + meu_nome)

#pode-se usar 'aspas simples' ou "aspas duplas" para Strings:
minha_idade = int(input('Entre com sua idade: '))

#também pode-se usar da virgula para concatenar no print
print('Sua idade é ', minha_idade)
print()


#   -----> Operadores Aritméticos <-----

x = float(input("Entre com x: "))
y = float(input("Entre com y: "))

soma = x + y
subtracao = x - y
multiplicacao = x * y
divisao = x / y
divisao_truncada = x // y #arredonda para baixo
exponenciacao = x ** y # x elevado a y
resto_divisao = x % y

print()

print("Soma:", soma)
print("Subtração:", subtracao)
print("Multiplicação:", multiplicacao)
print("Divisão:", divisao)
print("Divisão Truncada:", divisao_truncada)
print("Exponenciação:", exponenciacao)
print("Resto da Divisão:", resto_divisao)
print()


#   -----> Estruturas de decisão e operadores de comparação/lógicos <-----
'''
Estruturas de decisão são recursos da linguagem que permitem ao programador fazer determinadas ações de 
acordo com um predicado. Elas têm a seguinte sintaxe:

if condicao1:
    comandos
elif condicao2:
    comandos
elif condicao3:
    comandos
else:
    comandos

** Atenção! No Python, é necessário que os blocos estejam propriamente indentados, ou o 
    interpretador irá lançar um erro. **'''

if True:
    print('verdadeiro')
else:
    print('falso')
print()

#operadores de comparação
'''
Os operadores de comparação permitem verificar igualdades e desigualdades entre valores, sendo possível 
verificar se tal condição é verdadeira ou falsa. Dentre eles temos:

igual: x == y
diferente: x != y
menor: x < y
maior: x > y
menor_igual: x <= y
maior_igual: x >= y  '''

#operadores lógicos
'''
Os operadores lógicos são operadores que recebem `bools` como argumento e retornam um `bool`. 
Dentre eles podem destacar:

e_logico = x and y
ou_logico = x or y
nao_logico = not x  '''

x = float(input("Entre com um valor: "))
y = float(input("Entre com outro valor: "))

if x > y:
    print(x, ">", y)
elif x == y and x == 42:
    print("A resposta para a vida, o universo e tudo mais")
elif x < 0 or y < 0:
    print("Algum valor é negativo")
else:
    print("Nenhum bloco acima foi executado")
print()

#Outra coisa interessante é a capacidade do python de aninhar operadores de comparação:

x = float(input("Entre com um valor:"))

if 0 < x <= 10:
    print(x, "é maior que 0 e menor ou igual a 10")
elif -100 <= x <= 0:
    print(x, "está entre -100 e 0")
else:
    print(x, "é maior que 10 ou menor que -100")
print()


#   -----> Listas <-----
'''
No Python, pode-se criar listas heterogêneas (listas podem conter qualquer tipo de variável).   '''

lista1 = ["Multimídia", 100, True]
print(lista1)
print()

#Métodos e funções úteis para listas

lista2 = [42, "Python", 3.14159, lista1]

# Tamanho de uma lista:
print("Tamanho da lista:", len(lista2))
print()

# Adicionar um novo elemento:
lista2.append(1.88)
print("Lista com o novo elemento adicionado:", lista2)
print()

# Acessando valores individuais:
print("Elemento na posição 0:", lista2[0]) # Pega o elemento na posição 0.
print("Último elemento:", lista2[-1]) # Pega o último elemento.
print("Penúltimo elemento:", lista2[-2]) # Pega o penúltimo elemento.
print("Elemento na posição 2 e 3:", lista2[2:4]) # Pega os elementos 2 e 3. Obs.: Primeiro valor incluso e último excluso.

# Reverter lista:
lista2.reverse()
print("Lista invertida:", lista2)

# Ordenação (para listas homogêneas):
lista3 = [8, 4, 3, 10, -20]

lista3.sort()
print("Lista ordenada crescente:", lista3)

lista3.sort(reverse=True)
print("Lista ordenada decrescente:", lista3)
print()



#   -----> Estruturas de Repetição <-----
''' No python, temos duas estruturas de repetição: while e for'''

#While
x = 512

while x > 0:
    print("x =", x)
    x //= 2 # o mesmo que x = x // 2
print()
#For
lista2 = [42, "Python", 3.14159]

for valor in lista2:
    print(valor)
print()
print("[0, 5):")
for i in range(5):
    print(i)

print()

print("[2, 8):")
for j in range(2, 8):
    print(j)

print()

print("[4, 9) com passo 2:")
for k in range(4, 9, 2):
    print(k)
print()


#   -----> Tuplas <-----
''' Tuplas funcionam como listas heterogêneas de tamanho fixo e imutáveis. '''

louis = ("Louis XIV", "França")
beethoven = ("Beethoven", "Alemanha")
aristoteles = ("Aristóteles", "Grécia")

# Acessando valores:
print(louis[0])
print()

# Desconstrução de tuplas:
(nome1, pais1) = aristoteles
print(nome1, pais1)
print()



#   -----> Funções <-----
''' Funções fornecem uma forma de reutilizar o código e deixar ele mais organizado. A sintaxe é como abaixo: 

def nome_funcao(argumento1, argumento2, argumento3 = opcional1, argumento4 = opcional2):
    corpo_da_funcao
    return valor #obs.: return não é obrigatório
'''

# Função com retorno:
def soma(x, y=5):
    z = x + y
    return z

print(soma(1, 3))
print(soma(3))
print()

# Função sem retorno:
def mostra_paridade(valores):
    for valor in valores:
        if valor % 2 == 0:
            print(valor, "é par")
        else:
            print(valor, "é ímpar")

mostra_paridade(range(0, 10))
print()


#   -----> Funções anônimas <-----
''' Também chamadas de lambdas, são funções que podem ser salvas em váriaveis'''

mostra_pessoa = lambda nome, idade: nome + " tem " + str(idade) + " anos."
print(mostra_pessoa("Napoleão", 250))
print()

pontos = [(2, 5), (-1, 0), (6, 3), (2, -3)]
pontos_ordenados_em_x = sorted(pontos, key=lambda p: p[0])
print(pontos_ordenados_em_x)
print()


#   -----> Arrays do Numpy <-----
import numpy as np
'''           Vetores            '''
# Criação de vetores:
vetor = np.array([2, 3, 5, 7, 11])

# Shape mostra as dimensões do array:
print("Vetor:", vetor, "\nDimensão:", vetor.shape)
print()
# Também podemos especificar o tipo das variáveis dentro do array:
vetor_float = np.array([1, 0.1, 0.01, 0.001])
print("Vetor:", vetor_float, "   Dimensão:", vetor_float.shape, "   Tipo:", vetor_float.dtype)

print()

vetor_int = np.array([1, 1, 2, 3, 5, 8], np.uint8)
print("Vetor:", vetor_int, "               Dimensão:", vetor_int.shape, "   Tipo:", vetor_int.dtype)
print()
'''           Matrizes            '''
# Criação de matrizes:
matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print("Matriz:\n", matriz, "\n\nDimensão:", matriz.shape)
print()
''' Funções e operações relevantes: '''
#Criação de Arrays:
print('Array tamanho 2x4 preenchido com 1:')
print(np.ones((2, 4)))
print()
print('\nArray tamanho 2x4x3 preenchido com 0:')
print(np.zeros((3, 2, 4))) # Ordem invertida: [página, linha, coluna].
print()
print('\nArray 3x4 com valores aleatórios em [0, 10):')
np.random.seed(42) # Opcional.
print(np.random.randint(10, size=(3, 4)))
print()
print('\nArray com valores em [0, 1) e passo 0.1:')
print(np.arange(0, 1, 0.1))
print()
#Transposta e concatenação:
matriz_2x3 = np.array([[0, 1, 2], [3, 4, 5]])
print('Matriz 2x3:')
print(matriz_2x3)
print()
print('\nTransposta:')
print(matriz_2x3.T)
print()
matriz_2x2 = np.array([[6, 7], [8, 9]])
print('\nMatriz 2x2:')
print(matriz_2x2)
print()
matriz_3x3 = np.array([[6, 7, 8], [9, 10, 11], [12, 13, 14]])
print('\nMatriz 3x3:')
print(matriz_3x3)
print()
print('\nMatriz 2x3 e Matriz 3x3 - Concatenação no eixo das linhas (eixo 0):')
print(np.concatenate([matriz_2x3, matriz_3x3], axis=0))
print()
print('\nMatriz 2x3 e Matriz 2x2 - Concatenação no eixo das colunas (eixo 1):')
print(np.concatenate([matriz_2x3, matriz_2x2], axis=1))
print()
#Indexação (funciona da mesma forma que listas normais do python):
# Elementos individuais:
matriz_4x3 = np.array([[0,  1,  2],
                       [3,  4,  5],
                       [6,  7,  8],
                       [9, 10, 11]])

print("Linha de índice 0:", matriz_4x3[0]) # linha de índice 0
print("Linha 2 e coluna 1:", matriz_4x3[2, 1]) # linha de índice 2 ([6, 7, 8]) e coluna de índice 1
print("Todas linhas e coluna 1:", matriz_4x3[:, 1]) # todas as linhas e coluna de índice 1
print("Linhas [1, 3) e colunas >= 1:\n", matriz_4x3[1:3, 1:]) # linhas [1, 3), todas as colunas a partir de 1
print()
#Operações:
print('Multiplicação com escalar:')
print(np.ones((2, 3)) * 2)
print()
print('\nSoma com escalar:')
print(np.zeros(6) + 3)
print()
print('\nSoma ponto-a-ponto:')
# Equivalente a [[1, 1], [1, 1]] + [[10, 10], [10, 10]]:
print(np.ones((2, 2)) + 10 * np.ones((2, 2)))
print()
print('\nMultiplicação ponto-a-ponto:')
# Equivalente a [2, 2, 2, 2] * [5, 5, 5, 5]:
print((2 * np.ones(4)) * (5 * np.ones(4)))
print()
print('\nMultiplicação matricial:')
print(
    np.matmul(
        np.array([[1, 2],
                  [3, 4]]),
        np.array([[5, 6],
                  [7, 8]])))

print('\nProduto escalar:')
#Equivalente a 1 * (-1) + 2 * 0 + 3 * 1:
print(np.dot(np.array([1, 2, 3]), np.array([-1, 0, 1])))
print()
#######################################################################################################
'''         Exercícios        '''
''' 1. Crie dois arrays 8x8x3, com valores aleatórios do tipo np.uint8 no intervalo de 1 a 10 (inclusive): '''
print('Exercicio 1: ')
a = np.random.randint(low=0, high=11, size=(3, 8, 8), dtype=np.uint8)
b = np.random.randint(low=0, high=11, size=(3, 8, 8), dtype=np.uint8)
# Como o high é exclusivo, deve-se colocar um valor a mais (no caso 11) para gerar números
# entre 0 e 10.
print()
''' 2. Crie uma nova matriz `c`, cujos valores são as médias aritméticas dos valores (ponto-a-ponto) 
        das matrizes criadas no exercício 1.'''
print('Exercicio 2: ')
c = (a + b) / 2
print(c)
# a + b irá somar cada valor de a com cada valor de b. (a + b) / 2 irá finalmente dividir
# cada valor por 2.
print()
''' 3. Concatene as matrizes `a`, `b` e `c` horizontalmente, e depois guarde a subarray composta pelas linhas 
        1 a 7 (inclusive), colunas 0 a 3 (inclusive) e página 1.'''
# Dica: Ordem de acesso: [página (eixo 0), linha (eixo 1), coluna (eixo 2)].
print('Exercicio 3: ')
abc_concat = np.concatenate([a, b, c], axis=2)
d = abc_concat[1, 0:4, 1:8]
print(d)
print()
# Neste exemplo, o eixo de concatenação não alteraria o resultado, pois os índices de acesso usados
# estão se referindo à parte da matriz equivalente ao a.
# Note que os índices finais estão um a mais do que o proposto, visto que os índices são exlusivos.

''' 4. Multiplique a página 0 da matriz `a` com a página 1 da matriz `b` (faça multiplicação matricial).'''
print('Exercicio 4: ')
e = np.matmul(a[0], b[1])
print(e)
print()
# Alternativamente:
# e = np.matmul(a[0, :, :], b[1, :, :])

''' 5. Crie uma função que receba um array bidimensional e retorne uma tupla `(m, p)`, onde `m` é o maior 
        valor e `p` é a posição `(x, y)` no array onde se encontra `m`. Faça uso do `while` ou do `for` vistos acima. 
        Caso tenha mais de uma posição com valor máximo, utilize a posição mais antiga.'''
print('Exercicio 5: ')
# Dica: Infinito no numpy = np.inf

def max_index(array):
    m = -np.inf
    p = (None, None)  # obs.: None é um valor nulo, isto é, não-inicializado.
    (num_linhas, num_colunas) = array.shape[0:2]  # índices 0 e 1

    for i in range(num_linhas):
        for j in range(num_colunas):
            if array[i, j] > m:
                m = array[i, j]
                p = (i, j)
    return (m, p)

# Exemplo:
ex = np.random.randint(101, size=(4, 4))
(m, p) = max_index(ex)

print(ex)
print(m, p)
print()

''' 6. Pesquise sobre as funções `max`, `unravel_index` e `argmax` do NumPy e refaça o exercício 5 sem 
        utilizar estrutura de repetição.'''
print('Exercicio 6: ')
def max_index_fast(array):
    indice = np.argmax(array)
    p = np.unravel_index(indice, array.shape)
    #m = np.max(array)
    m = array[p] # mais eficiente do que usar np.max
    return (m, p)

# Exemplo:
(m, p) = max_index_fast(ex)

print(ex)
print(m, p)

# argmax retorna o índice do array como se ele tivesse primeiro se tornado um vetor (1 dimensão)
# Por exemplo, a posição (2, 1) de uma matrix 3x3 se tornaria 7 com o argmax (contando da esquerda
# para a direta, e de cima para baixo). unravel_index transforma novamente em um argumento
# em formato apropriado para a matriz.
# Uma coisa a se notar é que tal função funciona com qualquer array, não apenas arrays 2D.