import spacy
import json
import re
import unicodedata

def normalizar(texto):
    texto = texto.lower()
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')
    return texto

# Tenta carregar o modelo de língua portuguesa (médio)
try:
    pln = spacy.load("pt_core_news_md")
except:
    # Caso não esteja instalado no ambiente local, tenta baixar
    import subprocess
    subprocess.run(["python3", "-m", "spacy", "download", "pt_core_news_md"])
    pln = spacy.load("pt_core_news_md")

##### carregar dados médicos #####

try:
    with open("./model/medical_data.json", "r") as f:
        medical_data = json.load(f)
except FileNotFoundError:
    # Fallback para teste se o arquivo não estiver no local esperado
    with open("medical_data.json", "r") as f:
        medical_data = json.load(f)

##### funções auxiliares #####

def limpar_texto(texto):
    """
    Normaliza o texto removendo parênteses e convertendo para minúsculo.
    """
    texto = texto.lower()
    texto = re.sub(r"\(.*?\)", "", texto)
    return texto.strip()

def extrair_tokens_relevantes(doc):
    """
    Extrai apenas tokens que carregam significado (substantivos, adjetivos, verbos).
    Remove pontuação e stopwords.
    """
    return [token for token in doc if not token.is_stop and token.is_alpha]


##### motor de inferência #####

def diagnosticar(user_input):
    # Processa o input do usuário
    doc_user = pln(user_input)
    tokens_user = extrair_tokens_relevantes(doc_user)
    
    if not tokens_user:
        return []

    resultados = []

    for item in medical_data:
        doenca = item["doenca"]
        sintomas_doenca = item["sintomas"]
        tratamento = item["tratamento"]

        sintomas_encontrados = 0
        
        # Para cada sintoma da doença no banco de dados
        for sintoma_db in sintomas_doenca:
            sintoma_limpo = limpar_texto(sintoma_db)
            doc_sintoma = pln(sintoma_limpo)
            tokens_sintoma = extrair_tokens_relevantes(doc_sintoma)

            melhor_sim_para_este_sintoma = 0
            
            # Compara cada palavra relevante do usuário com as palavras do sintoma no DB
            for t_user in tokens_user:
                for t_sintoma in tokens_sintoma:
                    # Usa similaridade de vetores se disponível
                    if t_user.vector_norm and t_sintoma.vector_norm:
                        sim = t_user.similarity(t_sintoma)
                    else:
                        # Fallback para comparação exata de texto
                        sim = 1.0 if t_user.text == t_sintoma.text else 0.0
                    
                    if sim > melhor_sim_para_este_sintoma:
                        melhor_sim_para_este_sintoma = sim

            # Threshold de 0.75 é rigoroso o suficiente para evitar falsos positivos
            # mas flexível para variações linguísticas (ex: "febre" vs "febril")
            if melhor_sim_para_este_sintoma > 0.80: 
                sintomas_encontrados += 1

        if sintomas_encontrados > 0:
            # MÉTRICAS DE PRECISÃO:
            
            # 1. Cobertura da Doença: Quantos sintomas da doença o usuário tem?
            cobertura_doenca = sintomas_encontrados / len(sintomas_doenca)
            
            # 2. Precisão do Usuário: Dos sintomas que o usuário disse, quantos batem com esta doença?
            # Isso evita que doenças genéricas com muitos sintomas "ganhem" sempre.
            precisao_usuario = sintomas_encontrados / len(tokens_user)
            
            # Score final ponderado (70% precisão do que foi dito, 30% cobertura da doença)
            score_final = (precisao_usuario * 0.7) + (cobertura_doenca * 0.6)
            
            resultados.append({
                "sintomas": sintomas_doenca,
                "doenca": doenca,
                "score": score_final,
                "tratamento": tratamento
            })

    # Ordena por score e retorna os 3 melhores
    return sorted(resultados, key=lambda x: x["score"], reverse=True)[:6]

def encontrar_doenca_por_nome(input_usuario, diagnosticos):
    input_norm = normalizar(input_usuario)

    melhor_match = None
    melhor_score = 0

    for item in diagnosticos:
        nome_doenca = normalizar(item["doenca"])

        # Similaridade simples (podes evoluir para spaCy depois)
        if input_norm in nome_doenca or nome_doenca in input_norm:
            return item

        # Similaridade por palavras
        palavras_input = input_norm.split()
        palavras_doenca = nome_doenca.split()

        intersecao = set(palavras_input) & set(palavras_doenca)
        score = len(intersecao)

        if score > melhor_score:
            melhor_score = score
            melhor_match = item

    return melhor_match

##### interface #####

while True:
    user_input = input("\nDiga-me o que sentes (ou 'sair'): ")

    if user_input.lower() == "sair":
        break

    diagnosticos = diagnosticar(user_input)

    if not diagnosticos:
        print("\nNão foi possível encontrar um diagnóstico compatível.")
        continue

    print("\nPossíveis diagnósticos:\n")

    for r in diagnosticos:
        prob = round(r["score"] * 100, 1)
        print(f"- {r['doenca']} ({prob}%)")
        print(f"  Sintomas: {', '.join(r['sintomas'])}\n")

    print("Digite o nome da doença que mais se aproxima do que você está a sentir.")
    print("Exemplo: 'Estou com malária' ou apenas 'malária'")

    escolha_texto = input("\nSua escolha: ")

    # Limpeza básica da frase
    escolha_texto = re.sub(r"estou com|acho que é|tenho", "", escolha_texto.lower()).strip()

    selecionado = encontrar_doenca_por_nome(escolha_texto, diagnosticos)

    if selecionado:
        print("\n=== DIAGNÓSTICO SELECIONADO ===\n")
        print(f"Doença: {selecionado['doenca']}")
        print(f"Sintomas: {', '.join(selecionado['sintomas'])}")

        print("\nTratamento sugerido:")
        for t in selecionado["tratamento"]:
            print(f" - {t}")
    else:
        print("\nNão consegui identificar a doença que escolheste. Tenta escrever de forma mais simples.")