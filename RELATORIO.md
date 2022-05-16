# Relatório referente a tarefa de avaliação do sistema de busca

Foram comparadas duas versão do sistema de busca criado, uma versão utilizando o
stemmer de Poter (STEMMER) e uma versão sem a utilização de stemmer (NOSTEMMER).

O Gráfico de R-Precision compara o comportamento de ambos os sistemas de busca.
Valores próximos a 0 indicam que os sistemas de buscam deram resultados 
equivalentes para a query em questão. Valores positivos indicam uma maior
precisão relativa do sistema de busca STEMMER enquanto valores negativos indicam
uma maior precisão relativa do sistema de busca NOSTEMMER para a respectiva query.
![R-Precision STEMMER/NOSTEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/rprecision_stemmer_nostemmer_1.png)

## NOSTEMMER

![11 Points NOSTEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/11points_nostemmer_10.png)
![F1 NOSTEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/f1_nostemmer_11.png)
![Precision@5 NOSTEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/precision_at_5_nostemmer_12.png)
![Precision@10 NOSTEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/precision_at_10_nostemmer_13.png)
![MAP NOSTEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/avg_precision_map_nostemmer_14.png)
![MRR NOSTEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/reciprocal_rank_mrr_nostemmer_15.png)
![DCG NOSTEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/dcg_nostemmer_16.png)
![NDCG NOSTEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/ndcg_nostemmer_17.png)


## STEMMER

![11 Points STEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/11points_stemmer_2.png)
![F1 STEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/f1_stemmer_3.png)
![Precision@5 STEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/precision_at_5_stemmer_4.png)
![Precision@10 STEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/precision_at_10_stemmer_5.png)
![MAP STEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/avg_precision_map_stemmer_6.png)
![MRR STEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/reciprocal_rank_mrr_stemmer_7.png)
![DCG STEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/dcg_stemmer_8.png)
![NDCG STEMMER](https://github.com/carloscdias/COS738-BMT-irs_in_memory_vector_space_model/blob/main/avalia/ndcg_stemmer_9.png)
