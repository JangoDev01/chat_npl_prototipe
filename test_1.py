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


chat_data = spacy.load("pt_core_news_sm")
import pt_core_news_sm
chat_data = pt_core_news_sm.load()
doc = chat_data("Esta é uma frase.")
print([(w.text, w.pos_) for w in doc])