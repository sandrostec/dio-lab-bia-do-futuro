import json
import requests
import pandas as pd
import streamlit as st

# ================= CONFIGURAÇÃO =================

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"

# ================= CARREGAR DADOS =================

perfil = json.load(
    open("./data/perfil_investidor.json", encoding="utf-8")
)

recursos = json.load(
    open("./data/recursos_mia.json", encoding="utf-8")
)

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
Valor objetivo: R$ {perfil.get("valor_objetivo_principal")}
Valor economizado: R$ {perfil.get("valor_economizado")}

Hábito financeiro: {perfil.get("habito_financeiro")}
Nível de educação financeira: {perfil.get("nivel_educacao_financeira")}

METAS FINANCEIRAS:
{metas}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

HISTÓRICO DE INTERAÇÕES:
{historico.to_string(index=False)}

RECURSOS DISPONÍVEIS:
{json.dumps(recursos, ensure_ascii=False, indent=2)}
"""

# ================= SYSTEM PROMPT =================

SYSTEM_PROMPT = """
Você é a MIA – Mesada Inteligente Assistida.

Você é uma educadora financeira virtual especializada em ajudar crianças e adolescentes a administrar sua mesada.

OBJETIVO:

Auxiliar o usuário no controle da mesada, registro de gastos, acompanhamento de saldo, criação de metas financeiras, simulações simples de economia e aprendizado de educação financeira.

REGRAS:

1. Utilize apenas os dados fornecidos no contexto.
2. Nunca invente saldos, metas, gastos ou transações.
3. Se não houver informação suficiente, solicite mais detalhes.
4. Explique conceitos financeiros de forma simples.
5. Incentive hábitos saudáveis de economia.
6. Não recomende investimentos.
7. Não solicite senhas ou dados sensíveis.
8. Não realize transações financeiras.
9. Não julgue os gastos do usuário.
10. Priorize respostas educativas, claras e objetivas.
"""

# ================= CHAMAR O OLLAMA =================

def perguntar(msg):

    prompt = f"""
{SYSTEM_PROMPT}

CONTEXTO DO USUÁRIO:
{contexto}

PERGUNTA:
{msg}
"""

    resposta = requests.post(
        OLLAMA_URL,
        json={
            "model": MODELO,
            "prompt": prompt,
            "stream": False
        }
    )

    if resposta.status_code == 200:
        return resposta.json()["response"]

    return "Não foi possível obter resposta da MIA."

# ================= INTERFACE =================

st.set_page_config(
    page_title="MIA - Mesada Inteligente Assistida",
    page_icon="💰"
)

st.title("💰 MIA - Mesada Inteligente Assistida")

st.write(
    "Olá! Eu sou a MIA. Posso ajudar você a controlar sua mesada, acompanhar metas financeiras e aprender educação financeira."
)

if pergunta := st.chat_input("Digite sua dúvida sobre sua mesada..."):

    st.chat_message("user").write(pergunta)

    with st.spinner("MIA está pensando..."):
        resposta = perguntar(pergunta)

    st.chat_message("assistant").write(resposta)

# ================= SIDEBAR =================

with st.sidebar:

    st.header("👤 Usuário")

    st.write(f"**Nome:** {perfil.get('nome')}")
    st.write(f"**Idade:** {perfil.get('idade')} anos")
    st.write(f"**Saldo:** R$ {perfil.get('saldo_atual')}")
    st.write(f"**Meta principal:** {perfil.get('objetivo_principal')}")

    st.divider()

    st.header("🎯 Recursos")

    for recurso in recursos:
        st.write(f"• {recurso.get('nome')}")
