import spacy
import json
import re

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
            if melhor_sim_para_este_sintoma > 0.75: 
                sintomas_encontrados += 1

        if sintomas_encontrados > 0:
            # MÉTRICAS DE PRECISÃO:
            
            # 1. Cobertura da Doença: Quantos sintomas da doença o usuário tem?
            cobertura_doenca = sintomas_encontrados / len(sintomas_doenca)
            
            # 2. Precisão do Usuário: Dos sintomas que o usuário disse, quantos batem com esta doença?
            # Isso evita que doenças genéricas com muitos sintomas "ganhem" sempre.
            precisao_usuario = sintomas_encontrados / len(tokens_user)
            
            # Score final ponderado (70% precisão do que foi dito, 30% cobertura da doença)
            score_final = (precisao_usuario * 0.7) + (cobertura_doenca * 0.5)
            
            resultados.append({
                "sintomas": sintomas_doenca,
                "doenca": doenca,
                "score": score_final,
                "tratamento": tratamento
            })

    # Ordena por score e retorna os 3 melhores
    return sorted(resultados, key=lambda x: x["score"], reverse=True)[:3]

##### interface #####

user_input = input("Diga-me o que sentes para eu poder ajudar: ")
diagnosticos = diagnosticar(user_input)

if not diagnosticos:
    print("\nNão foi possível encontrar um diagnóstico compatível com os sintomas informados.")
else:
    print("\nPossíveis diagnósticos:\n")
    for r in diagnosticos:
        prob = round(r["score"] * 100, 1)
        print(f"Doença: {r['doenca']}")
        print(f"Sintomas: {', '.join(r['sintomas'])}")
        print(f"Confiança do Sistema: {prob}%")
        print("Tratamento Sugerido:")
        for t in r["tratamento"]:
            print(f" - {t}")
        print("-" * 40)