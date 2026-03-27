"""
    spacy - biblioteca de processamento de linguagem natural (chat_data) em Python
          - usada para tarefas como tokenização, análise sintática, reconhecimento de entidades nomeadas, etc
    link da documentação para instalação: https://spacy.io/usage
    comandos:
            pip install -U pip setuptools wheel - atualiza o pip, setuptools e wheel para garantir que você tenha as versões mais recentes
            pip install -U spacy - instala ou atualiza a biblioteca spacy
            python -m spacy download en_core_web_sm - baixa o modelo de linguagem em inglês (pequeno)
            python -m spacy download pt_core_news_sm - baixa o modelo de linguagem em português (pequeno)
            python -m spacy download pt_core_news_md - baixa o modelo de linguagem em português (médio) 
                - necessário para comparação de similaridade, pois o modelo pequeno não possui vetores de palavras
"""

import spacy
import pt_core_news_md as pt_data


## variavel que armazena o modelo de linguagem em português
pln = spacy.load("pt_core_news_sm")
pln = pt_data.load()

corpus_data = ["gato", "cachorro", "carro", "bicicleta", "avião",
               "computador", "telefone", "casa", "árvore", "flor",
               "livro", "caneta", "mesa", "cadeira", "janela",
               "porta", "rua", "cidade", "país", "mundo"]


user_input = input("Como possso te ajudar hoje: ")
doc = pln(f"{user_input}")



##### Buscando Semelhanças entre palavras #####
"""

"""

# cria um dicionário para mapear as palavras do corpus em minúsculas para suas formas originais (com acentos e maiúsculas)
corpus_lower = {word.lower(): word for word in corpus_data}

# iteração sobre os tokens do documento e comparação de similaridade com as palavras do corpus
for token in doc:
    if token.text.lower() in corpus_lower:
        word_original = corpus_lower[token.text.lower()]
        token2 = pln(word_original)[0]
        similaridade = round((token.similarity(token2) * 100), 2)
        print(f"A palavra '{token.text}' (do input) é {similaridade}% similar à palavra '{token2.text}' (do corpus)")