# -*- coding: utf-8 -*-

print("Olá mundo!")
print("Outra mensagem")
print("Mensagem 3")
# _______________________________________________________
"""Comentarios de muitas linhas"""

print(2 + 2)
print(2 / 2)
print(2 * 2)
print(2 ** 3)  # Exponenciação
print(10 % 3)  # Operadora módulo que nos dá o resto de uma operação de divisão
# _______________________________________________________
# Variáveis permitem o armazenamento de informação na memória

variavel = "Olá mundo"
print(variavel)

# Nome da variável não pode ter caracteres especiais e nem espaço. Podemos usar underline.
""" Tipos de variáveis:

Numérico inteiro: 47
Numérico flutuante: 12.89
Textual (spring): "Olá mundo"
Booleana: True or False """

var1 = 1  # variável inteira
var2 = 1.1  # variável float
var3 = "Eu sou uma string"  # variável string
var4 = True  # verdadeiro
var4 = False  # falso

print(var1)
print(var2)
print(var3)
print(var4)
# _______________________________________________________
"""Operadores matemáticos

+ = Adição
- = Subtração
* = Multiplicação
/ = Divisão
** = Exponenciação
% = Módulo

Exemplo: X = 10 (Se lê "x" recebe o valor de 10)
_______________________________________________________
Operadores Relacionais

== (Igual)
!= (Diferente)
> (Maior)
< (Menor)
>= (Maior ou Igual)
<= (Menor ou Igual) """

x = 2
y = 3

soma = x + y

print(x < y)
print(soma >= y)
"""______________________________________________________
Operadores Lógicos

AND - Comparar se suas condições são verdadeiras
OR - Comparar se pelo menos uma condição é verdadeira
NOR - Inverter o resultado dessas condições """

x = 3
y = 3
z = 4

print(x == y or x == z)

"""______________________________________________________
Comandos Condicionais ou Estruturas Condicionais

BLOCO = Trecho de código que depende de outro trecho

if: Realiza testes condicionais. Executa um bloxo SE uma determinada condição for atendida. Avalia se a condição é verdade ou não"""

x = 1
y = 1000000000

if x > y:
    print("x é maior que y")

if y > x:
    print("y é maior que x")

# else: É executado caso a condição do comando if não seja atendida

x = 1
y = 2

if x > y:
    print("x maior que y")
else:
    print("x não é maior que y")
# _________________________________________________________

a = 7
b = 6

if b > a:
    if b > 0:
        print("b é maior que a/nb é positivo")
    else:
        print("b não é maior que a nem positivo")
else:
    print("b menor que a")

# elif: Caso haja a necessidade de mais condições entre if e o else

x = 1
y = 2

if x == y:
    print("números iguais")
elif x < y:
    print("x menor que y")
elif y > x:
    print("y maior que x")
else:
    print("númetos diferentes")

""" Laços de repetição
- Estruturas de repetição
- Iteradores       iterar == repetir
- Repetem um trecho do código
	- Enquanto uma condição avaliada for verdadeira
	- Durante uma pré-determinada condição"""

x = 1

while x < 10:
    print(x)
    x += 1  # == x = x + 1

""" Listas: Sequências de números ou caracteres
for: Percorre um conjunto de dados pré estabelecidos. Para cada elemento da Lista,
a cada execução do laço for, o valor i será atribuído a uma das variáveis,contendo
todos os elementos da lista"""

Lista1 = [1, 2, 3, 4, 5]
Lista2 = ["ola", "mundo", "!"]
Lista3 = [0, "ola", "biscoito", "bolacha", 9.99, True]

for i in Lista1:
    print(i)

""" Combinar for com a função range, que nos retorna uma lista.
Podemos utilizar até 3 elementos na função range:

range(10) == Indica que haverá uma contagem de um 0 a 9, pois inicia-se com
zero, não contabilizando o dez;
range(10,20) == Indica que haverá uma contagem iniciando do 10 até o 20. Como
o ultimo elemento não é contabilizado, podemo considerar o último - 1.
range(10,20,2) == Indica que haverá uma contagem iniciando do 10 até 20
com intervalo de dois elementos de diferença """

for i in range(10, 20, 2):
    print(i)

""" Strings: Tipo especial de dados em que se armazena coleções de caracteres (texto)
São declaradas entre aspas ou apóstofres

var1 = 1        É um numeral
var2 = "1"		É uma string

- Concatenação: Strings aplicadas a duas variáveis"""

a = "Allef"
b = "Leal"

concatenar = a + " " + b
print(concatenar)

# Identificar o tamanho de uma string usando a func1ão len

a = "Allef"
b = "Leal"

concatenar = a + " " + b

tamanho = len(concatenar)
print(tamanho)

# Navegando pelo índice. Numeral da posição que eu quero exibir

a = "Allef"
b = "Leal"

concatenar = a + " " + b

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

# Imprimir um pedaço da string

a = "Allef"
b = "Leal"

concatenar = a + " " + b

print(concatenar[0:10])

""" Strings: Em Python, strings são objetos. Pode-se aplciar
métodos a strings

string = string.método()"""

# Função lower e upper para imprimir tudo em minúsculo ou maiúsculo

a = "Allef"
b = "Leal"

concatenar = a + " " + b

print(concatenar)
print(concatenar.lower())
print(concatenar.upper())

concatenar = concatenar.upper()
print(concatenar)

# Função strip para remover espaços/cacacteres especiais
# no começo e no fim da string

a = "Allef"
b = "Leal"

concatenar = a + " " + b + "\n"  # \n faz uma quebra de linha

print(concatenar)
print(concatenar.strip())

# Função split que converte uma string numa lista

minha_string = "O rato roeu a roupa do rei de Roma"

minha_lista = minha_string.split()
print(minha_lista)

minha_lista = minha_string.split("r")
print(minha_lista)
# .split("r") Quebra a string sem a letra r. Roma ficou com R, pois há a
# diferenciação de caracteres maiúsculos e minúsculos (case sensitive)

# Busca de substrings que é um pedaço de uma string
# Saber, por exemplo, em que posição aparece a palavra rei

minha_string = "O rato roeu a roupa do rei de Roma"

busca = minha_string.find("rei")
print(busca)
print(minha_string[busca:])

busca = minha_string.find("rainha")
print(busca)  # Retorna -1 nesse caso por não encontra a substring

# Substituir partes de uma string com o método replace

minha_string = "O rato roeu a roupa do rei de Roma"

minha_string = minha_string.replace("rei", "rainha")
print(minha_string)

""" Modularização - Funções
- Blocos de códigos executados apenas quando chamados

Em Python são definidas pela palavra reservada def

- Definição
def NOME(PARÂMETROS): COMANDOS

- Chamada
NOME(ARGUMENTOS) """


""" def soma(x, y):  # Sempre colocar as funções na parte de cima
    # type: (object, object) -> object
    return (x + y)

def multiplicação(x, y):
    return (x * y)"""


s = soma(2, 3)
print(s)

m = multiplicação(3, 4)
print(m)

print(soma(s, m))

""" Manipulação de arquivos

- Abrindo arquivos: utilizar a função open
 variavel = open(nome, modo)

 MODO     FUNÇÃO
 r________somente leitura
 w________escrita (caso o arquivo exista, será apagado e um novo criado)
 a________leitura e escrita (adiciona o novo conteúdo ao fim do arquivo)
 r+_______leitura e escrita
 w+_______escrita (o modo w+, assim com w, apaga o conteúdo anterior do arquivo)
 a+_______leitura e escrita (abre o arquivo para atualiazação)

Lendo arquivos

read() - Lê o arquivo inteiro
readline() - Lê uma linha
readlines() - Lê arquivo e o armazena em uma lista """

arquivo = open("arquivo.txt")
print(arquivo)

Linhas = arquivo.readlines()  # Pegou cada linha e jogou dentro de uma lista
print(Linhas)

for Linhas in Linhas:  # Imprimir linha por linha
    print(Linhas)

arquivo = open("arquivo.txt")
texto_completo = arquivo.read()  # Vai jogar tudo dentro de uma variável
print(texto_completo)

# É mais interessante utilizar a função readlines, pois já automaticamente
# converte numa lista

# Criar arquivo

w = open("arquivo.txt", "a")

w.write("Esse é o meu arquivo\n")
w.close()

""" Listas e Dicionários

Lista: representam conjuntps de dados como:
- Numérica: [1, 2, 3, 4, 5]
- Strings: ["bola", "sapato", "chuva"] """

minha_lista = ["abacaxi", "melancia", "abacate"]
minha_lista2 = [1, 2, 3, 4, 5]
minha_lista3 = ["abacaxi", 2, 9.89, True]

print(minha_lista[2])
print(minha_lista2[4])
print(minha_lista3[0])

for item in minha_lista2:
    print(item)

tamanho = len(minha_lista)
print(tamanho)

# Adicionando elementos a lista usando o método append

minha_lista = ["abacaxi", "melancia", "abacate"]
minha_lista2 = [1, 2, 3, 4, 5]
minha_lista3 = ["abacaxi", 2, 9.89, True]

minha_lista.append("limão")  # Adicionado o elemento criado ao final da lista
print(minha_lista)

# Verificar se um elemento pertence a uma lista


# Adicionando elementos a lista usando o método append

minha_lista = ["abacaxi", "melancia", "abacate"]
minha_lista2 = [1, 2, 3, 4, 5]
minha_lista3 = ["abacaxi", 2, 9.89, True]

minha_lista.append("limão")

if 3 in minha_lista2:
    print("3 está na lista")

# Removendo elementos

minha_lista = ["abacaxi", "melancia", "abacate"]
minha_lista2 = [1, 2, 3, 4, 5]
minha_lista3 = ["abacaxi", 2, 9.89, True]

minha_lista.append("limão")

del minha_lista[2:]  # Removendo do item 2 até o final
print(minha_lista)

del minha_lista[:]  # Remove todos os itens
print(minha_lista)

# Ordenar listas

lista = [124, 345, 5, 72, 46, 6, 7, 3, 1, 7, 0]
lista.sort()  # Ordena a lista numéricamente, alterando a lista original
print(lista)

lista = [124, 345, 5, 72, 46, 6, 7, 3, 1, 7, 0]
lista = sorted(lista)  # Retorna uma lista Ordenada
print(lista)

lista = [124, 345, 5, 72, 46, 6, 7, 3, 1, 7, 0]
lista.sort(reverse=True)  # Ordenar de maneira decrescente
print(lista)

lista = [124, 345, 5, 72, 46, 6, 7, 3, 1, 7, 0]
lista.reverse()  # Reverter a lista
print(lista)

lista2 = ["bola", "abacate", "dinheiro", "amor"]
lista2.sort()  # Nesse caso ordenou em ordem alfabética
print(lista2)

""" Dicionários
Em Python, dicionários são arrays associativos, ou seja, um determinado
valor passa a ser vinculado a uma chave. Exemplo:"""

dicionario_sites = {"Diego": "diegomariano.com"}  # a chave "Diego" foi vinculado ao valor "diegomariano.com"
print(dicionario_sites["Diego"])

# Se o dicionário tiver vários elementos, pode usar laços para imprimi-los:

dicionario_sites = {"Diego": "diegomariano.com", "Google": "google.com", "Udemy": "udemy.com"}
for chave in dicionario_sites:
    print(dicionario_sites[chave])

for i in dicionario_sites.items():
    print(i)

for i in dicionario_sites.keys():
    print(i)

# Escolha de número aleatórios a cada execução 

import random

numero = random.randint(0, 10)
print(numero)

random.seed(1)  # Para dar o mesmo resultado. Mas não é muito utilizado
numero = random.randint(0, 10)
print(numero)

lista = [6, 45, 9]
numero = random.choice(lista)  # Números da lista aleatórios a cada execução
print(numero)

# Tratamento de exceções

a = 2
b = 0

try:
    print(a / b)
except:
    print("Não é permitida a divisão por 0")

