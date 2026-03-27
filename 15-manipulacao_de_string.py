#### Strings 

# nome = "Miguel"
# funcao = "Desenvolvedor"

# ## Acessar um caracter numa determinada posição
# letra = nome[3]
# print(f"Letra na posição 3 da string {nome}:", letra)

# ## Tamanho da string
# tamanho_nome = len(nome)
# print(f"Tamanho da string {nome}:", tamanho_nome)

# ## concatenar strings
# concatenar_strings = nome + funcao
# print(concatenar_strings)

# ## fazer slicing (fatiamento) de strings
# slicing_string = "Super hiper mega treinamento python"
# print(f"Slicing da string {slicing_string} da posição 0 até a 4:", slicing_string[0:5])

# ## dividir strings em partes e agrupá-las em uma lista
# saudacao = "Olá, " + nome + "! Bem-vindo ao time de " + funcao + "."
# palavras = saudacao.split()
# print(palavras)
# print(palavras[2])  # Acessar o indece das palavras utilizando notação de colchetes

# ## interação com strings usando loops
# # Imprimir cada palavra da saudação com sua respectiva volta
# voltas = ["Primeira", "Segunda", "Terceira", "Quarta", "Quinta", "Sexta", "Sétima"]
# for palavra in palavras:
#     volta = voltas.pop(0) # Pega a primeira volta da lista e remove ela da lista
#     print(f"{volta} palavra da saudação: {palavra}")

# # imprimir cada caracter da string saudação
# for letra in saudacao:
#     print(letra)

# ## manipulando strings com o metodo find()
# email = input("Digite seu endereço de email: ")
# arroba = email.find('@')
# if arroba == -1: # verifica se o caracter @ foi encontrado
#     print("Endereço de email inválido. O caracter '@' não foi encontrado.")
# else:
#     usuario = email[0:arroba] # pega os caracteres do indece 0 até o indece do @
#     dominio = email[arroba + 1:] # pega todos os caracteres dos indeces após o @
#     print("Usuário:", usuario)
#     print("Domínio:", dominio)

# ## utilizando os operadores in e not in se existe uma sequencia de caracteres dentro de uma string
# produtos = "Arroz, Feijão, Macarrão, Açúcar, Sal"
# escolha = input("Digite o nome do produto que deseja buscar: ")
# if escolha.capitalize() in produtos:
#     print(produtos)
#     print(f"O produto '{escolha.capitalize()}' foi encontrado na lista.")
# elif escolha.capitalize() not in produtos:
#     print(f"O produto '{escolha.capitalize()}' não foi encontrado na lista.")
    
## tratamento de espaços em branco com os métodos strip(), lstrip() e rstrip()
texto = "           Olá, Mundo!         "
print(texto.lstrip()) # remove os espaços em branco à esquerda
print(texto.rstrip()) # remove os espaços em branco à direita
print(texto.strip())  # remove os espaços em branco à esquerda e à direita

## alinhamento de texto para exibição com os métodos center(), ljust() e rjust()
fruta = "Abacate"
print(fruta.rjust(20)) # Alinha à direita em um campo de 20 caracteres
print(fruta.center(20)) # Alinha ao centro em um campo de 20 caracteres
print(fruta.ljust(20)) # Alinha à esquerda em um campo de 20 caracteres

msg = "Olá"
print(msg.center(20, '=')) 

## trabalhando com prefixos e sufixos usando os métodos startswith() e endswith()
p = "O rato roeu a roupa do rei de Roma."
print(p.startswith("O"))
print(p.endswith("."))

## Docstring
"""
Docstring é uma string de documentação que descreve o propósito e o uso de um módulo, classe, método ou função em Python.
Ela é definida logo após a definição do objeto (módulo, classe, método ou função)
"""

## métodos úteis para manipulação de strings
