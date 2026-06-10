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

O arquivo `perfil_investidor.json` manteve sua nomenclatura original para preservar compatibilidade com a estrutura do projeto-base, porém seu conteúdo foi adaptado para representar o perfil financeiro educacional do usuário da MIA.

---

## Estratégia de Integração

### Como os dados são carregados?

Os arquivos JSON e CSV são carregados no início da aplicação utilizando Python.

Dessa forma, qualquer alteração realizada nos arquivos da pasta `data` é automaticamente refletida no contexto utilizado pela MIA.

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

Esses dados são utilizados para montar o contexto enviado ao agente, permitindo que a MIA responda de forma personalizada, coerente e sincronizada com as informações disponíveis nos arquivos da base.

---

### Como os dados são usados no prompt?

Os dados são utilizados como contexto complementar para a IA.

Antes de gerar uma resposta, a aplicação monta um bloco de contexto contendo informações do usuário, histórico de interações, transações, metas financeiras e recursos disponíveis.

```python
import json

def montar_contexto(perfil_usuario, historico_atendimento, transacoes, recursos_mia):

    metas = json.dumps(
        perfil_usuario.get("metas", []),
        ensure_ascii=False,
        indent=2
    )

    contexto = f"""
DADOS DO USUÁRIO:
Nome: {perfil_usuario.get("nome")}
Idade: {perfil_usuario.get("idade")}
Perfil financeiro: {perfil_usuario.get("perfil_financeiro")}
Tipo de usuário: {perfil_usuario.get("tipo_usuario")}
Mesada mensal: R$ {perfil_usuario.get("mesada_mensal")}
Saldo atual: R$ {perfil_usuario.get("saldo_atual")}
Objetivo principal: {perfil_usuario.get("objetivo_principal")}
Valor do objetivo principal: R$ {perfil_usuario.get("valor_objetivo_principal")}
Valor economizado: R$ {perfil_usuario.get("valor_economizado")}
Hábito financeiro: {perfil_usuario.get("habito_financeiro")}
Nível de educação financeira: {perfil_usuario.get("nivel_educacao_financeira")}

METAS FINANCEIRAS:
{metas}

ÚLTIMAS INTERAÇÕES:
{historico_atendimento.tail(5).to_string(index=False)}

TRANSAÇÕES RECENTES:
{transacoes.tail(10).to_string(index=False)}

RECURSOS DISPONÍVEIS:
{json.dumps(recursos_mia, ensure_ascii=False, indent=2)}
"""
    return contexto
```

Esse contexto é enviado para o modelo de IA, permitindo respostas mais personalizadas, coerentes e alinhadas às informações disponíveis.

---

## Exemplo de Contexto Gerado

O exemplo abaixo representa uma saída gerada automaticamente pela função `montar_contexto()`, utilizando os dados presentes nos arquivos da pasta `data`.

```text
DADOS DO USUÁRIO:
Nome: Pedro Silva
Idade: 12 anos
Perfil financeiro: aprendiz
Tipo de usuário: crianca_adolescente
Mesada mensal: R$ 100,00
Saldo atual: R$ 45,00
Objetivo principal: Comprar um jogo
Valor do objetivo principal: R$ 200,00
Valor economizado: R$ 80,00
Hábito financeiro: está aprendendo a controlar gastos
Nível de educação financeira: básico

METAS FINANCEIRAS:
- Comprar um jogo | Meta: R$ 200,00 | Economizado: R$ 80,00 | Prazo: 2026-06
- Comprar uma bicicleta | Meta: R$ 800,00 | Economizado: R$ 120,00 | Prazo: 2026-12
- Comprar um livro | Meta: R$ 60,00 | Economizado: R$ 25,00 | Prazo: 2026-03
- Comprar um fone de ouvido | Meta: R$ 150,00 | Economizado: R$ 40,00 | Prazo: 2026-05
- Comprar material escolar | Meta: R$ 120,00 | Economizado: R$ 30,00 | Prazo: 2026-02
- Ir ao cinema com amigos | Meta: R$ 80,00 | Economizado: R$ 20,00 | Prazo: 2026-04
- Comprar um controle para videogame | Meta: R$ 250,00 | Economizado: R$ 90,00 | Prazo: 2026-08

ÚLTIMAS INTERAÇÕES:
2025-11-18 | Compra planejada | Usuário simulou compra de um fone de ouvido
2025-11-22 | Controle de gastos | Usuário registrou compra de material escolar
2025-11-25 | Economia | Usuário solicitou sugestões para aumentar a economia mensal
2025-11-28 | Saldo disponível | Usuário consultou saldo após registrar novos gastos
2025-12-05 | Educação financeira | Usuário pediu explicação sobre orçamento pessoal

TRANSAÇÕES RECENTES:
2026-01-01 | Mesada mensal | R$ 100,00 | entrada
2026-01-03 | Lanche na escola | R$ 12,00 | saída
2026-01-05 | Sorvete | R$ 8,00 | saída
2026-01-10 | Presente da avó | R$ 50,00 | entrada
2026-01-25 | Depósito para meta financeira | R$ 30,00 | saída

RECURSOS DISPONÍVEIS DA MIA:
- Controle de Gastos
- Meta Financeira
- Simulador Financeiro
- Educação Financeira
- Consulta de Saldo
- Planejamento de Economia
```

---

## Benefícios da Estratégia

A utilização de uma base de conhecimento estruturada permite que a MIA:

* Personalize as respostas de acordo com o perfil do usuário;
* Considere o histórico de interações durante a conversa;
* Analise receitas, despesas, metas financeiras e hábitos de consumo;
* Realize simulações financeiras simples;
* Reduza respostas fora de contexto;
* Ofereça orientações mais educativas e consistentes.

Essa abordagem integra Inteligência Artificial Generativa, dados estruturados, Python e contexto personalizado, atendendo aos requisitos propostos pelo desafio.
