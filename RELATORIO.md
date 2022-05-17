# Relatório referente a tarefa de avaliação do sistema de busca

Foram comparadas duas versão do sistema de busca criado, uma versão utilizando o
stemmer de Porter (STEMMER) e uma versão sem a utilização de stemmer (NOSTEMMER).

Para os resultados que exibem Query #, nota-se que a query 93 não está no sistema,
quando analisado os dados e onde as queries foram extraídas, constatou-se que não
existe uma query com esta identificação.

O Gráfico de R-Precision compara o comportamento de ambos os sistemas de busca.
Valores próximos a 0 indicam que os sistemas de buscam deram resultados 
equivalentes para a query em questão. Valores positivos indicam uma maior
precisão relativa do sistema de busca STEMMER enquanto valores negativos indicam
uma maior precisão relativa do sistema de busca NOSTEMMER para a respectiva query.

![R-Precision STEMMER/NOSTEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/rprecision_stemmer_nostemmer_1.png)

De uma forma geral, o gráfico R-Precision indica que o sistema de busca
utilizando o stemmer de Porter obteve resultados mais precisos do que o sistema
de busca sem stemmer.

Abaixo são analisados os gráficos de 11 pontos, F1, Precision@5, Precision@10, 
MAP, MRR, DCG e NDCG para cada um dos sistemas de busca.


## 11 Points

O gráfico de 11-points interpolated average precision foi uma medida padrão das
competições TREC iniciais e trata-se de uma forma de visualizar a precisão e 
revocação em 11 níveis (0%, 10%, 20%, 30%, 40%, 50%, 60%, 70%, 80%, 90%, 100%)
facilitando a comparação da performance do buscador entre diferentes mecanismos
de busca. Para identificar um melhor buscador, procura-se neste gráfico a curva
superior, podendo ocorrer trade-offs a serem considerados na decisão quando as
curvas se intersectam.

Nos resultados encontrados, a curva do buscador STEMMER foi sempre maior que a
curva obtida para o buscador NOSTEMMER, indicando a melhor performance do 
primeiro.

### STEMMER
![11 Points STEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/11points_stemmer_2.png)

### NOSTEMMER
![11 Points NOSTEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/11points_nostemmer_10.png)

## F1

A métrica F associa as medidas de acurácia e revocação num único valor. No caso
particular do F1, atribui-se pesos iguais para ambas as medidas e a métrica
resultante se torna a média ponderada entre acurácia e revocação, assumindo
valores entre [0, 1]. Nos gráficos abaixo, a métrica F1 foi avaliada para 
cada consulta e pode-se observar que para um maior número de queries, o F1 
do buscador STEMMER possui melhor resultado quando comparado ao NOSTEMMER.

### STEMMER
![F1 STEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/f1_stemmer_3.png)

### NOSTEMMER
![F1 NOSTEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/f1_nostemmer_11.png)

## Precision@K

A métrica de Precision@K avalia a precisão dos K primeiros resultados da consulta.
Observa-se que tanto para as medidas de Precision@5 e Precision@10, o buscador
STEMMER obteve uma melhor performance quando considerada a média da métrica em
todas as consultas.

### STEMMER - Precision@5
![Precision@5 STEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/precision_at_5_stemmer_4.png)

### NOSTEMMER - Precision@5
![Precision@5 NOSTEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/precision_at_5_nostemmer_12.png)

### STEMMER - Precision@10
![Precision@10 STEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/precision_at_10_stemmer_5.png)

### NOSTEMMER - Precision@10
![Precision@10 NOSTEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/precision_at_10_nostemmer_13.png)

### MAP

A Mean Average Precision (MAP) considera a média do valor da precisão para os K
primeiros documentos encontrados a cada vez que um documento relevante é recuperado.

Os gráficos abaixo apresentam a medida Average Precision (AP) para cada busca.
O MAP calculado para cada gráfico de Precisão média x Query #, sendo este
a média da AP para todas as consultas, é exibido no título do gráfico do
respectivo buscador. O MAP calculado para ambos buscadores indicou a superioridade
do buscador STEMMER em relação ao NOSTEMMER para esta medida por um valor de 0,1
de diferença.

### STEMMER
![MAP STEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/avg_precision_map_stemmer_6.png)

### NOSTEMMER
![MAP NOSTEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/avg_precision_map_nostemmer_14.png)

### MRR

O Mean Reciprocal Rank (MRR) considera a métrica de Reciprocal Rank (RR) para o 
seu cálculo, sendo esta RR = 1/K, onde K é a posição do primeiro documento
relevante recuperado para a consulta. O MRR é então definido como a média do RR
para todas as consultas.

Os gráficos abaixo apresentam o RR x Query # para todas as consultas da coleção,
sendo o MRR calculado e exibido no título do gráfico obtido para cada buscador.
Os resultados apresentados indicam que para a maior parte das buscas, o primero
resultado retornado na resposta é relevante para a consulta para ambos buscadores.
Entretanto, há uma ligeira prevalência do buscador STEMMER, refletido por seu MRR
de 0,77, maior em 0,1 do que o buscador NOSTEMMER.

### STEMMER
![MRR STEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/reciprocal_rank_mrr_stemmer_7.png)

### NOSTEMMER
![MRR NOSTEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/reciprocal_rank_mrr_nostemmer_15.png)

### DCG

O Discounted Cumulative Gain (DCG) é baseado na premissa da utilidade de um documento,
onde documentos mais relevantes são muito mais úteis do que documentos 
marginalmente relevantes, dessa forma, quanto maior a posição de um documento na
lista retornada, menor é a sua utilidade. Para contabilizar a utilidade de um 
documento em relação à sua posição na resposta do buscador, o DCG é calculado como

![DCG Formula](https://latex.codecogs.com/svg.latex?DCG_p%20=%20rel_1%20+%20\sum_{i=1}^p%20\frac{rel_i}{log_2(i)})

Abaixo podem ser vistos a média do DCG em função de p para os buscadores STEMMER
e NOSTEMMER.
De acordo com os resultados apresentados, observa-se que os valores de DCG do
buscador STEMMER para cada ponto de p são maiores que os do buscador NOSTEMMER, 
indicando que os resultados mais úteis aparecem mais bem posicionados no primeiro
buscador.

### STEMMER
![DCG STEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/dcg_stemmer_8.png)

### NOSTEMMER
![DCG NOSTEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/dcg_nostemmer_16.png)

### NDCG

O Normalized Discounted Cumulative Gain (NDCG) evolui da ideia do DCG e considera
a presença de uma resposta ideal para a consulta, a qual usa para calcular um 
DCG ideal que é usado para normalizar o resultado obtido.

Os gráficos abaixo apresentam o NDCG x Query # para cada buscador analisado.
De modo geral, maiores valores de NDCG são observadas para as queries no buscador
STEMMER, o que também é confirmado pelo valor médio da métrica para todas as
consultas, mostrando a superioridade do buscador STEMMER em relação ao buscador
NOSTEMMER para a métrica de NDCG.

### STEMMER
![NDCG STEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/ndcg_stemmer_9.png)

### NOSTEMMER
![NDCG NOSTEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/ndcg_nostemmer_17.png)

