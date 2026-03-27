import spacy
import pt_core_news_md as pt_data
import json

with open("./model/medical_data.json", "r") as f:
    medical_data = json.load(f)

## variavel que armazena o modelo de linguagem em português
pln = spacy.load("pt_core_news_sm")
pln = pt_data.load()

corpus_data = [
    "Febre alta",
    "calafrios",
    "tosse seca",
    "dor de garganta",
    "mialgia (dores musculares)",
    "cefaleia (dor de cabeca)",
    "prostracao",
    "coriza",
    "ardor nos olhos",
    "Febre alta subita",
    "dor retro-orbitaria (atras dos olhos)",
    "mialgia intensa",
    "artralgia (dor nas articulacoes)",
    "exantema (manchas vermelhas)",
    "prurido",
    "fadiga",
    "nausea",
    "vomitos",
    "Febre",
    "tosse seca ou com catarro",
    "cansaco extremo",
    "perda de paladar (ageusia)",
    "perda de olfato (anosmia)",
    "dor de garganta",
    "falta de ar (dispneia)",
    "diarreia",
    "congestao nasal",
    "Febre alta",
    "tosse persistente",
    "coriza",
    "conjuntivite (olhos vermelhos e lacrimejantes)",
    "fotofobia",
    "manchas de Koplik (pequenos pontos brancos na mucosa bucal)",
    "exantema maculopapular avermelhado"
]


user_input = input("Como possso te ajudar hoje: ")
doc = pln(f"{user_input}")


##### Buscando Semelhanças entre palavras #####

# cria um dicionário para mapear as palavras do corpus em minúsculas para suas formas originais (com acentos e maiúsculas)
corpus_lower = {word.lower(): word for word in corpus_data}

# iteração sobre os tokens do documento e comparação de similaridade com as palavras do corpus
for token in doc:
    if token.text.lower() in corpus_lower:
        word_original = corpus_lower[token.text.lower()]
        token2 = pln(word_original)[0]
        similaridade = round((token.similarity(token2) * 100), 2)
        print(f"A palavra '{token.text}' (do input) é {similaridade}% similar à palavra '{token2.text}' (do corpus)")
        if similaridade >= 80:
            # 
            user_input_lower = user_input.lower()
            # iterando sobre os dados médicos para verificar se os sintomas do paciente são compatíveis com alguma doença
            for key, symptoms in medical_data.items():
                for symptom in symptoms:
                    if symptom.lower() in user_input_lower:
                        print(f"Os sintomas do paciente são compatíveis com a doença: {key}")

