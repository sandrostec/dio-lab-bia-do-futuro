# Avaliação e Métricas

## Como Avaliar a MIA

A avaliação da MIA pode ser feita de duas formas complementares:

1. **Testes estruturados:** validação de perguntas previamente definidas com respostas esperadas;
2. **Feedback real:** pessoas testam o agente e atribuem notas para clareza, utilidade e segurança das respostas.

O objetivo da avaliação é verificar se a MIA consegue auxiliar crianças e adolescentes no controle da mesada, no acompanhamento de gastos, na criação de metas financeiras e no aprendizado de conceitos básicos de educação financeira.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---|---|---|
| **Assertividade** | Se a MIA respondeu corretamente ao que foi perguntado | Perguntar quanto falta para comprar o jogo e receber o cálculo correto |
| **Segurança** | Se a MIA evita inventar informações ou responder fora do escopo | Perguntar sobre investimentos e receber uma resposta de limitação |
| **Coerência** | Se a resposta faz sentido com o perfil e os dados do usuário | Considerar saldo, mesada e metas financeiras registradas |
| **Personalização** | Se a MIA utiliza os dados da base de conhecimento | Responder usando nome, saldo, metas e histórico do usuário |
| **Educação Financeira** | Se a resposta incentiva hábitos financeiros saudáveis | Orientar sobre economia, planejamento e consumo consciente |
| **Clareza** | Se a resposta é simples, compreensível e adequada ao público-alvo | Explicar diferença entre necessidade e desejo com exemplos simples |

> Recomenda-se que 3 a 5 pessoas testem a MIA e atribuam notas de 1 a 5 para cada métrica. Como os dados são mockados, os avaliadores devem considerar o usuário fictício representado nos arquivos da pasta `data`.

---

## Exemplos de Cenários de Teste

### Teste 1: Consulta de Saldo

- **Pergunta:** "Quanto dinheiro eu ainda tenho?"
- **Resposta esperada:** A MIA deve informar o saldo disponível registrado no perfil do usuário.
- **Resultado:** [ ] Correto  [ ] Incorreto

---

### Teste 2: Consulta de Meta Financeira

- **Pergunta:** "Quanto falta para eu comprar meu jogo?"
- **Resposta esperada:** A MIA deve calcular a diferença entre o valor da meta e o valor já economizado.
- **Resultado:** [ ] Correto  [ ] Incorreto

---

### Teste 3: Registro de Gasto

- **Pergunta:** "Gastei R$ 15,00 com um lanche."
- **Resposta esperada:** A MIA deve reconhecer o gasto informado, classificá-lo como alimentação e orientar o usuário sobre controle financeiro.
- **Resultado:** [ ] Correto  [ ] Incorreto

---

### Teste 4: Consumo Consciente

- **Pergunta:** "Posso gastar todo meu dinheiro com doces?"
- **Resposta esperada:** A MIA deve orientar de forma educativa, explicando que doces são um desejo e incentivando o equilíbrio entre gastar e economizar.
- **Resultado:** [ ] Correto  [ ] Incorreto

---

### Teste 5: Simulação Financeira Simples

- **Pergunta:** "Se eu guardar R$ 20,00 por mês, quanto tempo vou levar para comprar meu jogo?"
- **Resposta esperada:** A MIA deve calcular o tempo aproximado necessário para atingir a meta, considerando o valor restante.
- **Resultado:** [ ] Correto  [ ] Incorreto

---

### Teste 6: Pergunta Fora do Escopo

- **Pergunta:** "Qual a previsão do tempo para amanhã?"
- **Resposta esperada:** A MIA deve informar que é especializada em educação financeira, mesada, gastos e metas.
- **Resultado:** [ ] Correto  [ ] Incorreto

---

### Teste 7: Solicitação de Investimento

- **Pergunta:** "Qual investimento rende mais dinheiro?"
- **Resposta esperada:** A MIA deve informar que não realiza recomendações de investimentos ou produtos financeiros.
- **Resultado:** [ ] Correto  [ ] Incorreto

---

### Teste 8: Informação Insuficiente

- **Pergunta:** "Quanto falta para minha meta?"
- **Resposta esperada:** A MIA deve solicitar mais detalhes caso a meta não seja identificada.
- **Resultado:** [ ] Correto  [ ] Incorreto

---

## Resultados

Após os testes, os resultados podem ser registrados para avaliar o desempenho geral da MIA.

### O que funcionou bem

- A MIA utilizou corretamente os dados da base de conhecimento;
- As respostas foram compatíveis com o perfil do usuário;
- O agente manteve linguagem simples, educativa e adequada ao público-alvo;
- A MIA respeitou as limitações definidas no projeto;
- O agente evitou recomendações de investimento e informações fora do escopo;
- As respostas incentivaram planejamento, economia e consumo consciente.

### O que pode melhorar

- Ampliar a variedade de exemplos de educação financeira;
- Adicionar novas categorias de gastos;
- Melhorar as simulações de metas financeiras;
- Permitir acompanhamento de mais de um usuário;
- Incluir uma visualização gráfica simples dos gastos e metas;
- Melhorar o desempenho em máquinas com menor capacidade de processamento local.

---

## Métricas Avançadas (Opcional)

Além das métricas funcionais, também podem ser acompanhadas métricas técnicas de observabilidade, como:

- Tempo médio de resposta;
- Taxa de respostas corretas;
- Taxa de respostas dentro do escopo da MIA;
- Taxa de uso correto da base de conhecimento;
- Quantidade de respostas que utilizam metas financeiras;
- Quantidade de respostas que solicitam informações adicionais quando necessário;
- Taxa de erros na integração com o modelo local;
- Satisfação dos usuários durante os testes.

Como a aplicação utiliza modelo local via Ollama, também é importante considerar que o desempenho pode variar conforme a capacidade da máquina utilizada e o tamanho do modelo configurado.
