# MIA – Mesada Inteligente Assistida

## Sobre o Projeto

A MIA (Mesada Inteligente Assistida) é uma agente de Inteligência Artificial criada para auxiliar crianças e adolescentes no controle da mesada, no acompanhamento de gastos, na criação de metas financeiras e no desenvolvimento de hábitos de consumo consciente.

O projeto foi desenvolvido como parte do desafio de IA Generativa, integrando documentação, engenharia de prompts, base de conhecimento estruturada, Python e experiência conversacional.

---

## Objetivo

Promover educação financeira de forma simples, segura e acessível, utilizando linguagem natural e exemplos adequados ao público infantojuvenil.

A MIA auxilia o usuário a:

* Controlar gastos da mesada;
* Acompanhar saldo disponível;
* Criar metas financeiras;
* Planejar compras futuras;
* Desenvolver hábitos de economia;
* Aprender conceitos básicos de educação financeira.

---

## Tecnologias Utilizadas

* Python
* Streamlit
* Ollama
* Inteligência Artificial Generativa
* JSON
* CSV
* Engenharia de Prompts

---

## Estrutura do Projeto

```text
data/
├── historico_atendimento.csv
├── perfil_investidor.json
├── recursos_mia.json
└── transacoes.csv

docs/
├── 01-documentacao-agente.md
├── 02-base-conhecimento.md
├── 03-prompts.md
├── 04-metricas.md
└── 05-pitch.md

src/
└── app.py
```

---

## Funcionalidades

* Consulta de saldo;
* Acompanhamento de metas financeiras;
* Simulações simples de economia;
* Orientações sobre consumo consciente;
* Educação financeira básica;
* Utilização de contexto personalizado baseado em JSON e CSV;
* Respostas contextualizadas com base nos dados do usuário.

---

## Segurança

A MIA foi projetada para atuar exclusivamente no contexto de educação financeira básica.

O agente:

* Não recomenda investimentos;
* Não realiza transações financeiras;
* Não solicita senhas ou dados bancários;
* Não acessa informações financeiras reais;
* Não fornece aconselhamento financeiro profissional.

---

## Como Executar

### 1. Instale as dependências

```bash
pip install streamlit pandas requests
```

### 2. Inicie o Ollama

Certifique-se de possuir um modelo compatível instalado, por exemplo:

```bash
ollama pull gpt-oss:20b
```

ou outro modelo compatível com sua máquina.

### 3. Execute a aplicação

```bash
streamlit run src/app.py
```

### 4. Acesse no navegador

```text
http://localhost:8501
```

---

## Estrutura da Solução

A MIA utiliza uma base de conhecimento composta por arquivos JSON e CSV contendo:

* Perfil do usuário;
* Histórico de interações;
* Transações financeiras simuladas;
* Recursos disponíveis do agente.

Essas informações são carregadas pela aplicação em Python e utilizadas como contexto para gerar respostas mais personalizadas, educativas e coerentes.

---

## Autor

**Sandro Cordeiro**

Projeto desenvolvido para fins educacionais como entrega do desafio **"Construa Seu Assistente Virtual Com Inteligência Artificial"** da DIO.
