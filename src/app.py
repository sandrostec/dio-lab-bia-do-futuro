import json
import requests
import pandas as pd
import streamlit as st

# ================= CONFIGURAÇÃO =================

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

st.set_page_config(
    page_title="MIA - Mesada Inteligente",
    page_icon="💰",
    layout="centered"
)

# ================= CARREGAR DADOS =================

perfil = json.load(open("./data/perfil_investidor.json", encoding="utf-8"))
recursos = json.load(open("./data/recursos_mia.json", encoding="utf-8"))

transacoes = pd.read_csv("./data/transacoes.csv")
historico = pd.read_csv("./data/historico_atendimento.csv")

# ================= MONTAR CONTEXTO =================

metas = json.dumps(
    perfil.get("metas", []),
    ensure_ascii=False,
    indent=2
)

contexto = f"""
DADOS DO USUÁRIO:
Nome: {perfil.get("nome")}
Idade: {perfil.get("idade")}
Perfil financeiro: {perfil.get("perfil_financeiro")}
Tipo de usuário: {perfil.get("tipo_usuario")}
Mesada mensal: R$ {perfil.get("mesada_mensal")}
Saldo atual: R$ {perfil.get("saldo_atual")}
Objetivo principal: {perfil.get("objetivo_principal")}
Valor do objetivo principal: R$ {perfil.get("valor_objetivo_principal")}
Valor economizado: R$ {perfil.get("valor_economizado")}
Hábito financeiro: {perfil.get("habito_financeiro")}
Nível de educação financeira: {perfil.get("nivel_educacao_financeira")}

METAS FINANCEIRAS:
{metas}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

HISTÓRICO DE INTERAÇÕES:
{historico.to_string(index=False)}

RECURSOS DISPONÍVEIS DA MIA:
{json.dumps(recursos, ensure_ascii=False, indent=2)}
"""

# ================= SYSTEM PROMPT =================

system_prompt = """
Você é a MIA – Mesada Inteligente Assistida, uma educadora financeira virtual e mentora financeira digital especializada em ajudar crianças e adolescentes a administrar sua mesada.

Seu objetivo é auxiliar o usuário no controle da mesada, registro de gastos, acompanhamento de saldo, criação de metas financeiras, simulações simples de economia e aprendizado de conceitos básicos de educação financeira.

REGRAS:
1. Sempre baseie suas respostas nos dados fornecidos no contexto.
2. Nunca invente valores, saldos, metas, gastos ou transações.
3. Se alguma informação não estiver disponível, diga que não possui dados suficientes e peça mais detalhes.
4. Explique conceitos financeiros de forma simples, usando exemplos do cotidiano.
5. Incentive hábitos saudáveis de economia, planejamento e consumo consciente.
6. Não julgue os gastos do usuário.
7. Não recomende investimentos, produtos bancários, crédito ou aplicações financeiras.
8. Não solicite senhas, dados bancários ou informações pessoais sensíveis.
9. Não realize transações financeiras.
10. Priorize respostas curtas, claras, educativas e seguras.
"""

# ================= FUNÇÃO PARA CHAMAR O MODELO =================

def perguntar_mia(pergunta):
    prompt = f"""
{system_prompt}

CONTEXTO DA BASE DE CONHECIMENTO:
{contexto}

PERGUNTA DO USUÁRIO:
{pergunta}

RESPONDA COMO A MIA:
"""

    payload = {
        "model": MODELO,
        "prompt": prompt,
        "stream": False
    }

    resposta = requests.post(OLLAMA_URL, json=payload)

    if resposta.status_code == 200:
        return resposta.json().get("response", "Não consegui gerar uma resposta.")
    else:
        return "Ocorreu um erro ao conectar com o modelo de IA."

# ================= INTERFACE STREAMLIT =================

st.title("💰 MIA - Mesada Inteligente Assistida")

st.write(
    "Olá! Eu sou a MIA, sua educadora financeira virtual. "
    "Posso ajudar você a controlar sua mesada, entender seus gastos e planejar suas metas."
)

pergunta = st.text_input("Digite sua pergunta:")

if st.button("Perguntar"):
    if pergunta.strip():
        with st.spinner("A MIA está pensando..."):
            resposta = perguntar_mia(pergunta)
            st.markdown("### Resposta da MIA")
            st.write(resposta)
    else:
        st.warning("Digite uma pergunta para continuar.")

# ================= INFORMAÇÕES LATERAIS =================

with st.sidebar:
    st.header("📌 Dados do Usuário")
    st.write(f"**Nome:** {perfil.get('nome')}")
    st.write(f"**Idade:** {perfil.get('idade')}")
    st.write(f"**Saldo atual:** R$ {perfil.get('saldo_atual')}")
    st.write(f"**Objetivo:** {perfil.get('objetivo_principal')}")

    st.header("🎯 Recursos da MIA")
    for recurso in recursos:
        st.write(f"- {recurso.get('nome')}")
