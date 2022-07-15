# Health Insurance Cross-Sell Prediction

<img src="https://github.com/nortonvanz/Health-Insurance-Ranking/blob/pa004_norton_vanz/images/insurance_recommendation.jpeg?raw=true" width=70% height=70% title="Health-Insurance-Ranking" alt="project_cover_image"/>

Projeto de rankeamento de clientes interessados na aquisição de um seguro veicular.

Contextualização:
Os dados do projeto foram obtidos do Kaggle, do desafio "Health Insurance Cross Sell Prediction".

Desta forma, o contexto de negócios é fictício, porém todo o planejamento e desenvolvimento da solução é implementado seguindo todos os passos de um projeto de mercado real.

## 1. Problema de negócios
### 1.1 Problema
A Insurance All é uma empresa tradicional de seguros de saúde.
Através de uma pesquisa, ela obteve retorno de 304 mil clientes sobre o interesse em adquirir um seguro veicular. O novo seguro foi desenvolvido, e está sendo ofertado aos interessados.

Porém existem mais 76 mil clientes, entre novos e antigos, que não responderam a pesquisa.
O call center já bastante atarefado, tem capacidade de contatar apenas 20 mil destes clientes potenciais.
Logo, precisa de uma lista ordenada por interesse destes 76 mil clientes, a fim de otimizar a conversão e o faturamento da empresa.

### 1.2 Objetivo
A partir dos dados de interesse em seguro veicular dos 304 mil clientes, construir um ranking por ordem de interesse (propensão de compra) dos 76 mil potenciais clientes.

As seguintes questões de negócio devem ser respondidas ao gestor do call center:

- Quais são os principais insights sobre os atributos mais relevantes de clientes interessados em seguro veicular?
- Qual a porcentagem de clientes interessados em seguro veicular, o call center conseguirá contatar fazendo 20 mil ligações?
- Se a capacidade do call center aumentar para 40 mil ligações, qual a porcentagem de clientes interessados em adquirir um seguro veicular o call center conseguirá contatar?
- Quantas ligações o call center precisa fazer para contatar 80% dos clientes interessados em adquirir um seguro veicular?

## 2. Premissas de negócio
- O time de vendas já utiliza o Google Sheets como ferramenta corporativa. É preciso que o ranking de propensão de compra seja incorporado nele.

## 3. Planejamento da solução
### 3.1. Produto final
O que será entregue efetivamente?
- Uma funcionalidade dentro da ferramenta Google Sheets, que ordena os 76 mil clientes (ou quaisquer novos clientes inclusos na planilha) por propensão de compra.

### 3.2. Ferramentas
Quais ferramentas serão usadas no processo?
- Python 3.8.12;
- Jupyter Notebook;
- Git, Github e Gitlab;
- Coggle Mindmaps;
- SweetViz;
- Heroku Cloud;
- Algoritmos de Regressão e Classificação;
- Pacotes de Machine Learning sklearn e xgboost;
- Técnicas de Seleção de Atributos;
- Flask e Python API's;
- Google Sheets Apps Script.

### 3.3 Processo
#### 3.3.1 Estratégia de solução
Com base no objetivo do projeto, trata-se portanto de um projeto de Learning to Rank (LTR).

Minha estratégia para resolver esse desafio, baseado na metodologia CRISP-DS, é detalhada pelo plano abaixo:

**Step 01. Data Description:**
- Coletar dados em um banco de dados na AWS Cloud.
- Compreender o significado de cada atributo dos interessados.
- Renomear colunas, compreender dimensões e tipos dos dados.
- Identificar e tratar dados nulos.
- Analisar atributos através de estatística descritiva.
- Separar 20% dos dados para teste (aleatoriamente, mas estratificados pela variável resposta).

**Step 02. Feature Engineering:**
- Criar mindmap de hipóteses de negócio.
- Realizar a feature engeneering, criando as features necessárias para validação das hipóteses.

**Step 03. Data Filtering:**
- Filtrar registros e atributos de acordo com restrições de negócio.

**Step 04. Exploratory Data Analysis:**
- Realizar uma análise univariada com uso do SweetViz, avaliando detalhes de cada atributo.
- Realizar uma análise bivariada, validando as hipóteses criadas e gerando insights de negócio.
- Criar tabela de resultados das hipóteses, e relevância estimada dos atributos para o aprendizado dos modelos.

**Step 05. Data Preparation:**
- Padronizar atributos numéricos com distribuição normal.
- Reescalar atributos numéricos com distribuição não normal.
- Codificar atributos categóricos em atributos numéricos.
- Aplicas as transformações acima aos dados de teste.

**Step 06. Feature Selection:**
- Separar dados de treino e validação.
- Rodar algoritmo para obter sugestão de atributos relevantes.
- Analisar o resultado em conjunto com os atributos relevantes estimado na EDA.
- Selecionar apenas os melhores atributos para treinar os modelos de machine learning.  

**Step 07. Machine Learning Modelling:**
- Rodar algoritmos: KNN classifier, Logistic regression, ExtraTrees classifier, e XGBboost classifier.
- Plotar curva de ganho cumulativo e lift, e calcular precison@k/recall@k de cada modelo.
- Criar tabela de performance comparando precison@k/recall@k de cada modelo.

**Step 08. Hyperparameter Fine Tunning:**
- Fazer um ajuste fino de hiperparâmetros em cada modelo, identificando o melhor conjunto de parâmetros para maximizar suas capacidades de aprendizagem.
- Aplicar validação cruzada em cada modelo, reduzindo o viés de seleção (teoria da amostragem), por utilizar várias amostras diferentes dos dados.
- Selecionar os 4 modelos com melhor conjunto de hiperparâmetros, e avaliar sua capacidade de aprendizagem.
- Plotar curvas de ganho cumulativo e lift, comparando os 4 modelos.
- Calcular precison@k/recall@k dos 4 modelos, e selecionar o de melhor performance.
- Submeter esse modelo aos dados de teste, e plotar suas curvas de ganho cumulativo e lift.
- Comparar precison@k/recall@k em treino vs. teste, avaliando a capacidade de generalização do modelo (aprendizado com dados inéditos).  

**Step 09. Convert Model Performance to Business Values:**
- Responder as questões de negócio do gestor ao call center.
- Comparar resultados da lista aleatória com a lista ordenada por propensão de compra.
- Traduzir a performance do modelo em resultados financeiros para a Insurance All.

**Step 10. Deploy Modelo to Production:**
- Criar as classes para publicação em produção.
- Testar as classes localmente.
- Publicar modelo no Heroku Cloud.
- Criar App Script em Google Sheets para consultar o modelo em produção.
- Implementar botão que consulta a propensão de compra dos clientes no Google Sheets, e testar a solução.


## 4. Os 3 principais insights dos dados
Durante a análise exploratória de dados, foram gerados insights ao time de negócio, através da validação das hipóteses.

Insights são informações novas, ou que contrapõe crenças até então estabelecidas do time de negócios. São também acionáveis, possibilitando ação para direcionar resultados futuros.

#### H1 - O interesse é maior em clientes com idade maior.

<img src="https://github.com/nortonvanz/Health-Insurance-Ranking/blob/pa004_norton_vanz/images/h1_age.png?raw=true" alt="h1_validacao" title="Interesse vs Idade" align="center" height="380" class="center"/>

Hipótese falsa. Pode ser observado que clientes entre 40-45 anos são os mais interessados em seguro veicular.

* Insight de negócio: Utilizar o conhecimento da faixa etária mais interessada em campanhas de marketing direcionadas.

#### H2 - O interesse é maior em clientes que possuem veículos mais novos.

<img src="https://github.com/nortonvanz/Health-Insurance-Ranking/blob/pa004_norton_vanz/images/h2_vehicle_age.png?raw=true" alt="h2_validacao" title="Interesse vs Idade do Veículo" align="center" height="380" class="center"/>

Hipótese falsa. Quando mais velho o veículo, maior é o interesse em seguro veicular:
- 4% dos clientes com veículos abaixo de 1 ano possuem interesse.
- 17% dos clientes com veículos entre 1 e 2 anos possuem interesse.
- 29% dos clientes com veículos com mais de 2 anos possuem interesse.

* Insight de negócio: Buscar dados de acionamento de seguro por clientes com veículos mais velhos, a fim de validar esta possível correlação. Havendo correlação, avaliar necessidade de reajustes no preço dos seguros ofertados a estes clientes.

#### 3 O interesse é maior em clientes que possuíam seu veículo previamente segurado.

<img src="https://github.com/nortonvanz/Health-Insurance-Ranking/blob/pa004_norton_vanz/images/h3_prev_insured.png?raw=true" alt="h3_validacao" title="Interesse vs Seguro Prévio" align="center" height="380" class="center"/>

Hipótese falsa. 22% dos clientes que não possuíam veículo previamente segurado estão interessados em seguro de veículo, enquanto apenas 1% dos clientes que possuíam seguro tem interesse.

* Insight de negócio: Obter informações sobre as condições dos seguros dos clientes que possuem seguro e não possuem interesse, realizando um benchmarking entre a oferta da Insurance All e a da concorrência, visando tornar-se mais atrativo a eles.

# 5. Modelo de Machine Learning aplicado

Na curva de ganho abaixo, são exibidos os 4 modelos com as melhores configurações de hiperparâmetros.
Também é exibido o modelo perfeito, que ordenaria todos os interessados em sequência no topo da lista.
Pro fim, o modelo de base é também exibido, representando a lista aleatória desordenada.

Curva de Ganhos Acumulados: ordenada por probabilidade de compra, cruza o percentual da base de clientes com o percentual de clientes propensos a comprar.
Ex: 40% da base de clientes (x), ordenada pela probabilidade de compra (y), contém 80% de todos os interessados em seguro veicular.

<img src="https://github.com/nortonvanz/Health-Insurance-Ranking/blob/pa004_norton_vanz/images/gains_curve_final%20.png?raw=true" alt="curva ganho final" title="Curva de Ganhos Acumulados - Comparação dos modelos" align="center" height="500" class="center"/>

Na curva lift abaixo, os 4 modelos somados ao modelo perfeito e o baseline também são exibidos.

Lift Curve: representa a diferença entre a curva de ganho e a lista aleatória. Portanto, informa o quanto o modelo é melhor que lista aleatória.
Ex: Abrangendo 40% da lista ordenada, o modelo é 2,2 vezes melhor que a lista aleatória.

<img src="https://github.com/nortonvanz/Health-Insurance-Ranking/blob/pa004_norton_vanz/images/lift_curves_final.png?raw=true" alt="curva lift final" title="Curva Lift - Comparação dos modelos" align="center" height="500" class="center"/>

Nas tabelas abaixo, precision@k e recall@k são exibidas para os diferentes modelos selecionados.

Precision@k: conta quantas previsões foram corretas até k e divide por todas as previsões feitas até k.

Ex: Precisão top 40% (ou 12196) k = 0,25 - Significa que em 40% da base, o modelo acertou 25% em relação ao modelo perfeito, que acertaria 60% no top 40%, sendo que depois de 12%, já capturou todos os interessados, e passaria a capturar apenas não interessados.

|Precision@|K-nearest neighbors|Logistic regression |Extra Trees classifier |Xgboost classifier |Perfect model |
|----------------|:----------:|:-------------------:|:---------------------------------:|:------------------:|:-------------:|
| 10% (3049) | 0.32 | 0.29 | 0.37 | 0.39 | 1 |
| 20% (6098) | 0.30 | 0.29 | 0.35 | 0.35 | 0.61 |
| 30% (9147) | 0.29 | 0.28 | 0.32 | 0.32 | 0.41 |
| 40% (12196)| 0.26 | 0.27 | 0.28 | 0.28 | 0.31 |

Recall@k: conta quantas previsões foram corretas até k e divide por todos os exemplos verdadeiros.

Ex: Recall top 40% (ou 12196) k = 0,8 - Significa que 80% do total de clientes interessados aparecem nos top 40% resultados da lista ordenada.

|Recall@|K-nearest neighbors|Logistic regression |Extra Trees classifier |Xgboost classifier |Perfect model |
|----------------|:------------------:|:-----------------------:|:-----------------------:|:----------------:|:-------------:|
| 10% (3049) | 0.26 | 0.24 | 0.30 | 0.32 | 0.82 |
| 20% (6098) | 0.49 | 0.47 | 0.56 | 0.57 | 1.00 |
| 30% (9147) | 0.71 | 0.68 | 0.78 | 0.78 | 1.00 |
| 40% (12196)| 0.86 | 0.88 | 0.92 | 0.93 | 1.00 |

O melhor modelo portanto foi o XGBoost Classifier, e por isso foi eleito para deploy em produção.

# 6. Performance do modelo de Machine Learning
Com o uso dos dados de teste (dados inéditos), é feita a simulação de performance do modelo em ambiente de produção.

As curvas de ganho cumulativo e lift dos dados de teste são apresentadas abaixo.

<img src="https://github.com/nortonvanz/Health-Insurance-Ranking/blob/pa004_norton_vanz/images/gain_lift_test_final.png?raw=true" alt="curva lift final" title="Curva Lift - Comparação dos modelos" align="center" height="700" class="center"/>

Na sequência, as duas tabelas demonstram os valores de precision@k e recall@k do XGBoost.

É possível observar que comparando-se o modelo de treino e validação com o modelo de teste, as métricas permaneceram muito parecidas.

|Precision@|Xgboost classifier (train)|Xgboost classifier (test)
|----------------|:---------------:|:------------------:|
| 10% | 0.39 | 0.38 |
| 20% | 0.35 | 0.35 |
| 30% | 0.32 | 0.32 |
| 40% | 0.28 | 0.28 |

|Recall@|Xgboost classifier (train)|Xgboost classifier (test)
|----------------|:---------------:|:------------------:|
| 10% | 0.32 | 0.31 |
| 20% | 0.57 | 0.56 |
| 30% | 0.78 | 0.78 |
| 40% | 0.93 | 0.92 |

Isto evidencia que o modelo tem uma boa capacidade de generalização, ou seja, é capaz de aprender com dados nunca antes vistos.


# 7. Resultados de Negócio

Dos 76.220 clientes, 9.340 estão interessados em seguros de veículos. (12,25% do total)
O ticket médio para um seguro de saúde anual da Insurance All é: $ 31669.

Vamos assumir todos os clientes interessados no seguro veicular irão assinar o contrato, e que o valor médio do seguro do veículos será o mesmo do seguro saúde.

As questões de negócios abaixo serão respondidas com base nas premissas citadas.

### Qual a porcentagem de clientes interessados em seguro veicular, o call center conseguirá contatar fazendo 20 mil ligações?

<img src="https://github.com/nortonvanz/Health-Insurance-Ranking/blob/pa004_norton_vanz/images/20k_calls_results.png?raw=true" alt="20 k calls" title="Resultados com 20 mil ligações" align="center" height="700" class="center"/>

Pela lista aleatória:
 - A equipe de vendas contata 26% dos interessados em seguro veicular: 2.451 clientes (ver Ganho: cruzamento linha preta x verde).
  ==> Receita estimada: 2.451 * 31.669 = US$ 77,62 milhões por ano.

Pela lista ordenada (modelo):
 - A equipe de vendas contata 70% dos interessados em seguro veicular: 6.576 clientes (ver Ganho: cruzamento linha azul x verde).
  ==> Receita estimada: 6.576 * 31.669 = US$ 208,26 milhões por ano.

RESULTADO: O modelo é 2,68 vezes melhor que a lista aleatória (ver Lift: linha azul x verde).
Portanto, a receita estimada é 2,68 vezes maior que a lista aleatória: US$ 130,63 milhões.


### Se a capacidade do call center aumentar para 40 mil ligações, qual a porcentagem de clientes interessados em adquirir um seguro veicular o call center conseguirá contatar?

<img src="https://github.com/nortonvanz/Health-Insurance-Ranking/blob/pa004_norton_vanz/images/40k_calls_results.png?raw=true" alt="40 k calls" title="Resultados com 40 mil ligações" align="center" height="700" class="center"/>

Pela lista aleatória:
  - A equipe de vendas contata 52% dos interessados em seguro veicular: 4902 clientes (ver Ganho: cruzamento linha preta x verde).
  ==> Receita estimada = 4902 * 31669 = US$ 155,24 milhões por ano.

Pela lista ordenada (modelo):
  - A equipe de vendas contata 99,5% dos interessados em seguro veicular: 9.294 clientes (ver Ganho: cruzamento linha azul x verde).
  ==> Receita estimada: 9.291 * 31.669 = US$ 294,24 milhões por ano.

RESULTADO: O modelo é 1,9 vezes melhor que a lista aleatória (ver Lift: cruzamento linha azul x verde).
Portanto, a receita estimada é 1,9 vezes maior que a lista aleatória: US$ 139 milhões.


### Quantas ligações o call center precisa fazer para contatar 80% dos clientes interessados em adquirir um seguro veicular?

<img src="https://github.com/nortonvanz/Health-Insurance-Ranking/blob/pa004_norton_vanz/images/80perc_cust_results.png?raw=true" alt="80% interessados" title="Resultados com 80% dos interessados" align="center" height="700" class="center"/>

Pela lista aleatória:
  - A equipe de vendas precisa fazer 60.976 ligações, para entrar em contato com 80% dos clientes da lista, então atingirá 80% dos interessados em seguro veicular.

Pela lista ordenada (modelo):
  - A equipe de vendas precisa fazer 23.800 ligações, para entrar em contato com 31% dos clientes da lista, então atingirá 80% dos interessados em seguro veicular (ver Ganho: cruzamento linha azul x verde).

RESULTADO: Fazendo 23800 ligações, o modelo é 2,6 vezes melhor que a lista aleatória. (ver Lift: cruzamento linha azul x verde).


### Planilha funcional em Google Sheets

<img src="/images/gif_800.gif" alt="cumulative gains curve and lift curve" title="Demonstração da solução" align="center" height="600" class="center"/>

Acesso a planilha: [Google Sheets - Health Insurance Ranking](https://docs.google.com/spreadsheets/d/1GM-Ul_8zbroP7pNapIoZuXfV3NJNghgihs9lYQiDqPI/edit#gid=0)


# 8. Conclusões

Com base nos resultados de negócio, conclui-se que o objetivo do projeto foi alcançado.

Com a solução de dados entregue, a Insurance All possui agora uma vantagem competitiva frente aos seus concorrentes, reduzindo o custo de aquisição de clientes, e aumentando o seu faturamento.

Pelo fato da solução implementada via planilha poder ser utilizada para novos clientes que ainda nem foram conquistados, é esperado um incremento ainda maior no faturamento esperado.  

É possível ainda aproveitar a solução para simular perfis de clientes, funcionalidade que é de grande valia para a empresa.

# 9. Melhorias futuras
- Criar mais atributos a partir dos já existentes, buscando gerar mais insumos para o aprendizado dos modelos.
- Utilizar mais de um método de seleção de atributos, incluindo o Boruta ou o RFECV por exemplo.
- Utilizar o Optuna no hyperparameter fine tunning, visando otimizar os modelos.

## 10 Referências
* O Dataset foi obtido no [Kaggle](https://www.kaggle.com/datasets/anmolkumar/health-insurance-cross-sell-prediction).
* A imagem utilizada é de uso livre e foi obtida no [Pexels](https://www.pexels.com/pt-br/foto/onibus-branco-ao-lado-da-estrutura-de-concreto-2889806/).
