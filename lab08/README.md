# Lab08 - Modelo Lógico e Análise de Dados em Grafos

## Equipe Brazilian Research of Atmosphere Towards Health - BReATH
* Gabriel Costa Kinder - 234720
* Elton Cardoso do Nascimento - 233840
* João Pedro de Moraes Bonucci - 218733
* Lucas Otávio Nascimento de Araujo - 240106

## Modelo Lógico Combinado do Banco de Dados de Grafos
> ![Modelo Lógico de Grafos](images/modelo-logico-grafos.png)

## Perguntas de Pesquisa/Análise Combinadas e Respectivas Análises
### Pergunta/Análise 1
> * Probabilidade de infecção esta relacionada com local da residencia? | Existe um aumento de casos em determinada estação do ano?
>   
>   * Explicação sucinta da análise que será feita no grafo para atender à pergunta. Deve ser indicado explicitamente em qual das modalidades a análise se encaixa: centralidade; vulnerabilidade; comunidade/modularidade; motifs; predição de links.

### Pergunta/Análise 2
* Alterações do tempo atmosférico influenciam no conjunto de sintomas mais comuns de algumas doenças respiratórias
    * Ao assumir que teremos um grafo bipartido que relaciona estados climáticos com sintomas podemos procurar pelas maiores centralidades dentre os estados climáticos. Existindo algum padrão de variação onde uma específica mudança aparece múltiplas vezes nestes nós centrais poderemos concluir sua relação entre a causa destes sintomas.

### Pergunta/Análise 3
* É possível antecipar flutuações no número de casos de doenças respiratórias a partir da previsão do tempo?
   * Assumindo que tal relação exista, podemos, ao obter um novo dado relacionado a um estado climático, utilizar uma técnica de predição de links para antecipar, em média, a quantia e os sintomas que serão apresentados durante os próximos dias nas estações de saúde de uma localização geográfica específica.
