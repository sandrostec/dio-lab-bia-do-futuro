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

Os arquivos JSON e CSV são carregados no início da aplicação utilizando Python. Dessa forma, qualquer alteração feita nos arquivos da pasta `data` será refletida automaticamente no contexto montado para a MIA.

```python
import json
import pandas as pd

def carregar_base_conhecimento():
    historico_atendimento = pd.read_csv("data/historico_atendimento.csv")
    transacoes = pd.read_csv("data/transacoes.csv")

    with open("data/perfil_investidor.json", "r", encoding="utf-8") as f:
        perfil_usuario = json.load(f)

    with open("data/recursos_mia.json", "r", encoding="utf-8") as f:
        recursos_mia = json.load(f)

    return perfil_usuario, historico_atendimento, transacoes, recursos_mia
```

Esses dados são utilizados para montar o contexto enviado ao agente, permitindo que a MIA responda de forma personalizada, coerente e sincronizada com as informações disponíveis nos arquivos da base.

---

### Como os dados são usados no prompt?

Os dados são utilizados como contexto complementar para o agente.

O perfil do usuário, o histórico de atendimento, as transações e os recursos da MIA são organizados dinamicamente em um bloco de contexto antes da geração da resposta.

```python
import json

def montar_contexto(perfil_usuario, historico_atendimento, transacoes, recursos_mia):
    ultimas_interacoes = historico_atendimento.tail(5).to_string(index=False)
    transacoes_recentes = transacoes.tail(10).to_string(index=False)
    recursos_formatados = json.dumps(recursos_mia, ensure_ascii=False, indent=2)

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
Nível de educação financeira: {perfil_usuario.get("nivel_educacao_financeira")}

ÚLTIMAS INTERAÇÕES:
{ultimas_interacoes}

TRANSAÇÕES RECENTES:
{transacoes_recentes}

RECURSOS DISPONÍVEIS DA MIA:
{recursos_formatados}
"""

    return contexto
```

Esse contexto pode ser incluído no prompt da IA para orientar a resposta da MIA, garantindo maior personalização e reduzindo o risco de respostas fora do escopo.

---

## Exemplo de Integração Completa

O exemplo abaixo demonstra como a aplicação pode carregar os arquivos da pasta `data` e montar o contexto automaticamente.

```python
perfil_usuario, historico_atendimento, transacoes, recursos_mia = carregar_base_conhecimento()

contexto_mia = montar_contexto(
    perfil_usuario=perfil_usuario,
    historico_atendimento=historico_atendimento,
    transacoes=transacoes,
    recursos_mia=recursos_mia
)

print(contexto_mia)
```

Com essa abordagem, as informações exibidas no contexto não ficam fixas manualmente na documentação. Elas são preenchidas automaticamente pelo Python a partir dos arquivos:

* `perfil_investidor.json`
* `historico_atendimento.csv`
* `transacoes.csv`
* `recursos_mia.json`

---

## Modelo de Contexto Gerado

O modelo abaixo representa a estrutura do contexto gerado automaticamente pela função `montar_contexto()`.

```text
DADOS DO USUÁRIO:
Nome: valor carregado de perfil_investidor.json
Idade: valor carregado de perfil_investidor.json
Perfil financeiro: valor carregado de perfil_investidor.json
Tipo de usuário: valor carregado de perfil_investidor.json
Mesada mensal: valor carregado de perfil_investidor.json
Saldo atual: valor carregado de perfil_investidor.json
Objetivo principal: valor carregado de perfil_investidor.json
Valor do objetivo principal: valor carregado de perfil_investidor.json
Valor economizado: valor carregado de perfil_investidor.json
Nível de educação financeira: valor carregado de perfil_investidor.json

ÚLTIMAS INTERAÇÕES:
últimos registros carregados de historico_atendimento.csv

TRANSAÇÕES RECENTES:
últimos registros carregados de transacoes.csv

RECURSOS DISPONÍVEIS DA MIA:
dados carregados de recursos_mia.json
```

A partir desse contexto sincronizado com os arquivos da base, a MIA consegue responder perguntas como:

* Quanto ainda tenho de saldo?
* Quanto gastei este mês?
* Quanto falta para minha meta?
* Como posso economizar melhor?
* Esse gasto é uma necessidade ou um desejo?

Essa estratégia permite que o agente utilize dados estruturados para gerar respostas contextualizadas, educativas, seguras e sempre alinhadas ao conteúdo atualizado dos arquivos da base de conhecimento.
