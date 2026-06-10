# Base de Conhecimento

## Dados Utilizados

A base de conhecimento da MIA foi estruturada com arquivos da pasta `data`, contendo dados simulados para contextualizar as interações, personalizar respostas e apoiar simulações financeiras simples.

| Arquivo                   | Formato | Utilização no Agente                                    |
| ------------------------- | ------- | ------------------------------------------------------- |
| historico_atendimento.csv | CSV     | Contextualizar interações anteriores com a MIA          |
| perfil_investidor.json    | JSON    | Armazenar o perfil financeiro educacional do usuário    |
| recursos_mia.json         | JSON    | Descrever os recursos disponíveis na MIA                |
| transacoes.csv            | CSV     | Registrar entradas, saídas e padrão de gastos da mesada |

> Os dados utilizados são mockados e possuem finalidade exclusivamente educacional.

---

## Adaptações nos Dados

Os dados originais foram adaptados para o contexto da MIA – Mesada Inteligente Assistida.

Foram removidas referências a produtos financeiros, investimentos e perfil de investidor tradicional. No lugar, foram criados dados relacionados a mesada, gastos, metas financeiras, saldo disponível, recursos educacionais e histórico de interações.

As informações foram ajustadas para representar uma experiência de educação financeira simples, segura e adequada para crianças e adolescentes.

O arquivo perfil_investidor.json manteve sua nomenclatura original para preservar compatibilidade com a estrutura do projeto-base, porém seu conteúdo foi adaptado para representar o perfil financeiro educacional do usuário da MIA.

---

## Estratégia de Integração

### Como os dados são carregados?

Os arquivos JSON e CSV são carregados no início da aplicação utilizando Python.

```python
import json
import pandas as pd

# Carregando arquivos CSV
historico_atendimento = pd.read_csv("data/historico_atendimento.csv")
transacoes = pd.read_csv("data/transacoes.csv")

# Carregando arquivos JSON
with open("data/perfil_investidor.json", "r", encoding="utf-8") as f:
    perfil_usuario = json.load(f)

with open("data/recursos_mia.json", "r", encoding="utf-8") as f:
    recursos_mia = json.load(f)
```

Esses dados são usados para montar o contexto enviado ao agente, permitindo que a MIA responda de forma mais personalizada e coerente com as informações disponíveis.

---

### Como os dados são usados no prompt?

Os dados são utilizados como contexto complementar para o agente.

O perfil do usuário, o histórico de atendimento, as transações e os recursos da MIA são organizados em um bloco de contexto antes da geração da resposta.

```python
def montar_contexto(perfil_usuario, historico_atendimento, transacoes, recursos_mia):
    contexto = f"""
DADOS DO USUÁRIO:
Nome: {perfil_usuario.get("nome")}
Idade: {perfil_usuario.get("idade")}
Perfil financeiro: {perfil_usuario.get("perfil_financeiro")}
Mesada mensal: R$ {perfil_usuario.get("mesada_mensal")}
Saldo atual: R$ {perfil_usuario.get("saldo_atual")}
Objetivo principal: {perfil_usuario.get("objetivo_principal")}

ÚLTIMAS INTERAÇÕES:
{historico_atendimento.tail(5).to_string(index=False)}

TRANSAÇÕES RECENTES:
{transacoes.tail(10).to_string(index=False)}

RECURSOS DISPONÍVEIS DA MIA:
{json.dumps(recursos_mia, ensure_ascii=False, indent=2)}
"""
    return contexto
```

Esse contexto pode ser incluído no prompt da IA para orientar a resposta da MIA, garantindo maior personalização e reduzindo o risco de respostas fora do escopo.

---

## Modelo de Contexto Montado

O modelo abaixo demonstra como a função `montar_contexto()` organiza dinamicamente os dados carregados dos arquivos da pasta `data`.

Os valores entre chaves são preenchidos automaticamente pelo Python no momento da execução, a partir dos arquivos `perfil_investidor.json`, `historico_atendimento.csv`, `transacoes.csv` e `recursos_mia.json`.

```text
DADOS DO USUÁRIO:
Nome: {perfil_usuario.get("nome")}
Idade: {perfil_usuario.get("idade")}
Perfil financeiro: {perfil_usuario.get("perfil_financeiro")}
Mesada mensal: R$ {perfil_usuario.get("mesada_mensal")}
Saldo atual: R$ {perfil_usuario.get("saldo_atual")}
Objetivo principal: {perfil_usuario.get("objetivo_principal")}

ÚLTIMAS INTERAÇÕES:
{historico_atendimento.tail(5).to_string(index=False)}

TRANSAÇÕES RECENTES:
{transacoes.tail(10).to_string(index=False)}

RECURSOS DISPONÍVEIS DA MIA:
{json.dumps(recursos_mia, ensure_ascii=False, indent=2)}
