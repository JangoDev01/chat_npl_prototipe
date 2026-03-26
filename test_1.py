"""
    spacy - biblioteca de processamento de linguagem natural (chat_data) em Python
          - usada para tarefas como tokenização, análise sintática, reconhecimento de entidades nomeadas, etc
    link da documentação para instalação: https://spacy.io/usage
    comandos:
            pip install -U pip setuptools wheel - atualiza o pip, setuptools e wheel para garantir que você tenha as versões mais recentes
            pip install -U spacy - instala ou atualiza a biblioteca spacy
            python -m spacy download en_core_web_sm - baixa o modelo de linguagem em inglês (pequeno)
            python -m spacy download pt_core_news_sm - baixa o modelo de linguagem em português (pequeno)
"""

import spacy
import pt_core_news_sm as pt_data


## variavel que armazena o modelo de linguagem em português
pln = spacy.load("pt_core_news_sm")
pln = pt_data.load()

user_input = input("Digite uma frase para análise: ")
# u - prefixo para indicar que a string é uma string Unicode (importante para lidar com caracteres acentuados em português)
doc = pln(f"{user_input}")


"""
    iteração sobre os tokens do documento e impressão de suas características (texto, parte do discurso, lema e dependência sintática)
    pos_ - parte do discurso dos tokens (ex: substantivo, verbo, adjetivo, etc)
    lemma_ - forma base ou canônica do token (ex: "correr" para "correndo")... Útil para análise de texto, pois permite agrupar palavras com a mesma raiz.
    dep_ - relação de dependência sintática do token em relação a outros tokens na frase (ex: sujeito, objeto, predicado, etc).
"""
for token in doc:
    print(f"Token: {token.text}, POS: {token.pos_}, Lemma: {token.lemma_}, Dep: {token.dep_}")

## imprime uma lista de tuplas contendo o texto do token e sua respectiva parte do discurso (POS)
# print([(w.text, w.pos_) for w in doc])