# Análise de Transações Fraudulentas

Este projeto consiste em uma análise exploratória de um conjunto de dados relacionado a transações de cartão de crédito.

## Objetivos

- Dominar o ambiente de desenvolvimento e SVM. 
- Problematização conforme os dados colhidos. 
- Solução. 
- Explorar funções de modelagem de dados. 
- Explorar com percentual de base de testes. 
- Exibir dados em gráficos utilizando alguma biblioteca de exibição de dados. 
- Com base no dataset escolhido, aplicar ao modelo os algoritmos SVC, KNN e Árvore. 
- Avaliar a diferença da Acurácia entre os percentuais de testes.
- Criar uma apresentação com os dados colhidos e analises realizadas.


## Conjunto de Dados

O Dataset útilizado foi obtido no Kaggle e contém informações de transações, registradas em uma Fintech nos Estados unidos entre 21/06/2020 a 28/06/2020.
O arquivo CSV pode ser encontrado [aqui](https://www.kaggle.com/datasets/kelvinkelue/credit-card-fraud-prediction).


## Bibliotecas Utilizadas

- pandas
- numpy
- matplotlib

## Passos do Projeto

O projeto segue os seguintes passos:
1. **Carregamento e Exploração Inicial dos Dados**: Os dados são carregados em um DataFrame pandas e os primeiros registros são visualizados para entender sua estrutura.
2. **Exploração de funcionalidades**: Iremos utilizar algumas funções da biblioteca Pandas para analisar os dados, sendo elas: .head(), .tail(), .describe(), .info(), dropna().
3. **Limpeza de Dados**: São identificados e removidos registros com dados inconsistentes, como idades negativas ou superiores a 100 anos.
4. **Análise Estatística Descritiva**: São calculadas estatísticas descritivas básicas para as variáveis como horario das transações, como idade, categorias, valor e Estado.
5. **Visualização**: São criados gráficos para visualizar a distribuição das variáveis.
6. **Preparação dos Dados para Modelagem**: As variáveis preditoras são selecionadas e padronizadas para garantir que estejam na mesma escala para modelagem de machine learning.


## Como Executar o Código

1. Clone o repositório em sua máquina local.
2. Certifique-se de ter as bibliotecas mencionadas instaladas em seu ambiente Python.
3. Execute o arquivo Python `analise-cc.py` para reproduzir a análise.

## Acesso notebook google colab

- Clique [aqui](https://colab.research.google.com/drive/15FOFJ1ClajqPHFe1FJE19YGcrJ82RgGY?usp=sharing) para ter acesso ao código.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request com sugestões de melhorias.
