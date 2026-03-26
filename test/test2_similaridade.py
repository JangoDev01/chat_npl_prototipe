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


user_input = input("Como possso te ajudar hoje: ")
doc = pln(f"{user_input}")

##### Buscando Semelhanças entre palavras #####
"""

"""
for token in doc:
    for token2 in doc:
        similaridade = round((token.similarity(token2) * 100),2)
        print(f"A palavra {token.text} é {similaridade}% similar à palavra {token2.text}")