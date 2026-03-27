import spacy
import pt_core_news_md as pt_data
import json

# carregar modelo
pln = spacy.load("pt_core_news_md")
pln = pt_data.load()

# carregar dados médicos
with open("./model/medical_data.json", "r", encoding="utf-8") as f:
    medical_data = json.load(f)

# input do usuário
user_input = input("Como posso te ajudar hoje: ")
doc_user = pln(user_input)
# processar tokens do usuário, removendo stop words e pontuação
tokens_user = [token.text.lower() for token in doc_user if not token.is_stop and token.is_alpha]
# criar objetos Doc para cada token do usuário
docs_user_tokens = [pln(token) for token in tokens_user]

doenca_provavel = None
maior_similaridade = 0
melhor_tratamento = None

# iterar sobre as doenças no nosso arquivo JSON
for item in medical_data:
    doenca = item["doenca"]
    sintomas = item["sintomas"]
    tratamento = item["tratamento"]

    similaridade_max_doenca = 0

    # loop para comparar com cada sintoma digitado pelo usuário
    for sintoma in sintomas:
        doc_sintoma = pln(sintoma)

        similaridades = []

        for doc_token in docs_user_tokens:
            if doc_token.vector_norm and doc_sintoma.vector_norm:
                sim = doc_token.similarity(doc_sintoma)
            else:
                # fallback simples
                sim = 1 if doc_token.text in sintoma.lower() else 0

            similaridades.append(sim)

        # pega a melhor correspondência para esse sintoma
        similaridade = max(similaridades) if similaridades else 0

        if similaridade > similaridade_max_doenca:
            similaridade_max_doenca = similaridade

    # verificar se essa doença é a melhor até agora
    if similaridade_max_doenca > maior_similaridade:
        maior_similaridade = similaridade_max_doenca
        doenca_provavel = doenca
        melhor_tratamento = tratamento

# definir um threshold mínimo (evita respostas ruins)
if maior_similaridade >= 0.6:
    print("\nDoença mais provável:", doenca_provavel)
    print(f"Similaridade: {round(maior_similaridade * 100, 2)}%")

    print("\nTratamento recomendado:")
    for t in melhor_tratamento:
        print("-", t)
else:
    print("Não foi possível identificar uma doença com confiança.")