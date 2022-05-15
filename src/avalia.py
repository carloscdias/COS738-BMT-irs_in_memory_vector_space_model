#!python3
import ast
import csv
from collections import defaultdict
from utils import init_irs, get_stemmer
import numpy as np
from matplotlib import pyplot as plt

# 1. Gráfico de 11 pontos de precisão e recall
# 2. F1
# 3. Precision@5
# 4. Precision@10
# 5. Histograma de R-Precision (comparativo)
# 6. MAP
# 7. MRR
# 8. Discounted Cumulative Gain (médio)
# 9. Normalized Discounted Cumulative Gain

def eleven_points_graph(expected, results):
    expected_set = set([e[0] for e in expected])
    total_expected = len(expected_set)
    precision = []
    recall = []
    found = 0
    for i, r in enumerate(results):
        if r[0] in expected_set:
            found += 1
        p = found/(i + 1)
        r = found/total_expected
        precision.append(p)
        recall.append(r)
    # calculate points with interpolation
    result = np.zeros((11,))
    j = 0
    for i in range(11):
        while recall[j] < i*0.1 and j < len(recall) - 1:
            j += 1
        result[i] = max(precision[j:])
    return result

def main():
    config, logger = init_irs('AVALIA')
    logger.info('starting "avalia"...')

    logger.info('reading evaluation engine configuration...')
    results_filename = config['RESULTADOS']
    expected_filename = config['ESPERADOS']
    output_dir = config['OUTPUT']
    stemmer_option = config['STEMMER']
    stemmer = get_stemmer(stemmer_option)

    results = defaultdict(list)
    expected = defaultdict(list)

    logger.info(f'parsing results in "{results_filename}"')
    with open(results_filename, newline='') as results_file:
        results_csv = csv.reader(results_file, delimiter=';')
        for query_number, str_list in results_csv:
            ranking_pos, doc_number, ranking = ast.literal_eval(str_list)
            results[int(query_number)].append((int(doc_number), ranking_pos, ranking))

    logger.info(f'parsing expected in "{expected_filename}"')
    with open(expected_filename, newline='') as expected_file:
        expected_csv = csv.reader(expected_file, delimiter=';')
        header = expected_csv.__next__()
        for query_number, doc_number, doc_votes in expected_csv:
            expected[int(query_number)].append((int(doc_number), int(doc_votes)))

    # sort query results based on doc_votes
    for k in expected:
        expected[k].sort(reverse=True, key=lambda x: x[1])

    # 11 points graph precision recall
    queries = list(results.keys())
    n_queries = len(queries)
    eleven_points_pr = np.zeros((11, n_queries))

    for i, q in enumerate(queries):
        eleven_points_pr[:, i] = eleven_points_graph(expected[q], results[q])

    # plot 11 point graph
    data = eleven_points_pr.mean(axis=1)
    plt.figure(figsize=(10, 8), dpi=100)
    plt.grid()
    fontsize = 12
    plt.xlabel('Revocação', fontsize=fontsize)
    plt.ylabel('Precisão', fontsize=fontsize)
    plt.title(f'Avaliação do mecanismo de busca ({stemmer_option} - média de {n_queries} queries)', fontsize=16, pad=30)
    plt.plot(np.arange(0, 1.1, 0.1), data)
    plt.savefig(f'{output_dir}/11_points_precision_recall.pdf')
    plt.show()


if __name__ == '__main__':
    main()

