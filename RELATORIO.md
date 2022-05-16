# Relatório referente a tarefa de avaliação do sistema de busca

Foram comparadas duas versão do sistema de busca criado, uma versão utilizando o
stemmer de Porter (STEMMER) e uma versão sem a utilização de stemmer (NOSTEMMER).

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

### STEMMER
![11 Points STEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/11points_stemmer_2.png)

### NOSTEMMER
![11 Points NOSTEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/11points_nostemmer_10.png)

## F1

### STEMMER
![F1 STEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/f1_stemmer_3.png)

### NOSTEMMER
![F1 NOSTEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/f1_nostemmer_11.png)

## Precision@5

### STEMMER
![Precision@5 STEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/precision_at_5_stemmer_4.png)

### NOSTEMMER
![Precision@5 NOSTEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/precision_at_5_nostemmer_12.png)

## Precision@10

### STEMMER
![Precision@10 STEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/precision_at_10_stemmer_5.png)

### NOSTEMMER
![Precision@10 NOSTEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/precision_at_10_nostemmer_13.png)

### MAP

### STEMMER
![MAP STEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/avg_precision_map_stemmer_6.png)

### NOSTEMMER
![MAP NOSTEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/avg_precision_map_nostemmer_14.png)

### MRR

### STEMMER
![MRR STEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/reciprocal_rank_mrr_stemmer_7.png)

### NOSTEMMER
![MRR NOSTEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/reciprocal_rank_mrr_nostemmer_15.png)

### DCG

### STEMMER
![DCG STEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/dcg_stemmer_8.png)

### NOSTEMMER
![DCG NOSTEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/dcg_nostemmer_16.png)

### NDCG

### STEMMER
![NDCG STEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/ndcg_stemmer_9.png)

### NOSTEMMER
![NDCG NOSTEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/ndcg_nostemmer_17.png)

