#!python3
import ast
import csv
import re
from collections import defaultdict
from utils import init_irs
import numpy as np
from matplotlib import pyplot as plt

# 1. Gráfico de 11 pontos de precisão e recall  - OK
# 2. F1                                         - OK
# 3. Precision@5                                - OK
# 4. Precision@10                               - OK
# 5. Histograma de R-Precision (comparativo)    - OK
# 6. MAP                                        - OK
# 7. MRR                                        - OK
# 8. Discounted Cumulative Gain (médio)         - OK
# 9. Normalized Discounted Cumulative Gain      - OK

SHOULD_PLOT = True

def precision_recall(expected, results):
    expected_set = set([e[0] for e in expected])
    result_set = set([r[0] for r in results])
    found = len(expected_set & result_set)
    precision = found/len(result_set)
    recall = found/len(expected_set)
    return (precision, recall)

def f1(expected, results):
    total_queries = len(results)
    data = np.zeros((2, total_queries))
    for i, query_number in enumerate(results.keys()):
        p, r = precision_recall(expected[query_number], results[query_number])
        data[0, i] = query_number
        data[1, i] = 0 if (p + r) == 0 else (2*p*r)/(p + r)
    return data

def r_precision(expected, results1, results2):
    total_queries = len(expected)
    data = np.zeros((2, total_queries))
    for i, q in enumerate(expected.keys()):
        k = len(expected[q])
        p1, _ = precision_recall(expected[q], results1[q][:k])
        p2, _ = precision_recall(expected[q], results2[q][:k])
        data[0, i] = q
        data[1, i] = p1 - p2
    return data

def normalized_discounted_cumulative_gain(expected, results, p = 10):
    total_queries = len(results)
    log_arr = np.log2([2] + list(range(2, p + 1)))
    non_normalized = np.zeros((p, total_queries))
    normalized = np.zeros((p, total_queries))
    for i, query_number in enumerate(results.keys()):
        # for dcg the rank should be [0, r] where r > 2
        # since the rank here is a percentage, we multiply
        # its value for 100 to respect the constraint
        rank = np.array([100.0*r[2] for r in results[query_number][:p]])
        # add articial non-relevant documents
        rank_arr = np.zeros((p,))
        for j, v in enumerate(rank):
            rank_arr[j] = v
        # for comparison we have to put the ideal rank in the
        # same range as ours, this rank in particular is [0, 4]
        # so multiplying for 25 puts them in the same range
        ideal = np.array([25.0*e[1] for e in expected[query_number][:p]])
        # add articial non-relevant documents
        ideal_arr = np.zeros((p,))
        for j, v in enumerate(ideal):
            ideal_arr[j] = v
        total = np.cumsum(rank_arr/log_arr)
        non_normalized[:, i] = total 
        normalized[:, i] = total/np.cumsum(ideal_arr/log_arr)
    x = np.arange(1, p + 1)
    return (np.vstack([x, normalized.mean(axis=1)]), np.vstack([x, non_normalized.mean(axis=1)])) 

def reciprocal_rank(expected, results, limit = 100):
    total_queries = len(results)
    data = np.zeros((2, total_queries))
    for i, query_number in enumerate(results.keys()):
        expected_set = set([e[0] for e in expected[query_number]])
        found = 0
        for k, r in enumerate(results[query_number]):
            if k >= limit:
                break
            if r[0] in expected_set:
                data[1, i] = 1/(k + 1)
                break
        data[0, i] = query_number
    return data

def avg_precision(expected, results):
    total_queries = len(results)
    data = np.zeros((2, total_queries))
    for i, query_number in enumerate(results.keys()):
        expected_set = set([e[0] for e in expected[query_number]])
        total_p = 0
        found = 0
        for j, r in enumerate(results[query_number]):
            if r[0] in expected_set:
                found += 1
                total_p += found/(j + 1)
        data[0, i] = query_number
        data[1, i] = 0.0 if found == 0 else total_p/found
    return data

def precision_at(k, expected, results):
    total_queries = len(results)
    data = np.zeros((2, total_queries))
    for i, query_number in enumerate(results.keys()):
        expected_set = set([e[0] for e in expected[query_number]])
        result_set = set([r[0] for r in results[query_number][:k]])
        p, _ = precision_recall(expected[query_number], results[query_number][:k])
        data[0, i] = query_number
        data[1, i] = p
    return data

def eleven_points_graph(expected, results):
    n_queries = len(results)
    eleven_points_pr = np.zeros((11, n_queries))
    for k, q in enumerate(results.keys()):
        expected_set = set([e[0] for e in expected[q]])
        total_expected = len(expected_set)
        precision = []
        recall = []
        found = 0
        for i, r in enumerate(results[q]):
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
        eleven_points_pr[:, k] = result
    return np.vstack([np.arange(0, 1.1, 0.1), eleven_points_pr.mean(axis=1)])

def plot_data(data, title, xlabel, ylabel, xlim, filename, graph=plt.plot):
    fontsize = 12
    plt.figure(figsize=(10, 8), dpi=100)
    plt.grid()
    plt.xlabel(xlabel, fontsize=fontsize)
    plt.ylabel(ylabel, fontsize=fontsize)
    plt.title(title, fontsize=16, pad=30)
    graph(data[0, :], data[1, :])
    plt.xlim(xlim)
    plt.savefig(filename)
    if SHOULD_PLOT:
        plt.show()

def save_data_in_csv(data, filename):
    with open(filename, 'w', newline='') as file_ref:
        file_csv = csv.writer(file_ref, delimiter=';')
        file_csv.writerow(['X', 'Y'])
        for line in data.T:
            file_csv.writerow(line)

def main():
    global SHOULD_PLOT
    config, logger = init_irs('AVALIA')
    logger.info('starting "avalia"...')

    logger.info('reading evaluation engine configuration...')
    compare = re.split('\s*,\s*', config['COMPARE'])
    results_filename = [config['RESULTADOS'].replace('$', c) for c in compare] 
    expected_filename = config['ESPERADOS']
    output_dir = config['OUTPUT']
    SHOULD_PLOT = config.getboolean('PLOT')

    results = {}
    expected = defaultdict(list)

    for i, c in enumerate(compare):
        results[c] = defaultdict(list)
        logger.info(f'parsing results in "{results_filename[i]}"')
        with open(results_filename[i], newline='') as results_file:
            results_csv = csv.reader(results_file, delimiter=';')
            for query_number, str_list in results_csv:
                ranking_pos, doc_number, ranking = ast.literal_eval(str_list)
                results[c][int(query_number)].append((int(doc_number), ranking_pos, ranking))

    logger.info(f'parsing expected in "{expected_filename}"')
    with open(expected_filename, newline='') as expected_file:
        expected_csv = csv.reader(expected_file, delimiter=';')
        header = expected_csv.__next__()
        for query_number, doc_number, doc_votes in expected_csv:
            expected[int(query_number)].append((int(doc_number), int(doc_votes)))

    # sort query results based on doc_votes
    for k in expected:
        expected[k].sort(reverse=True, key=lambda x: x[1])

    s = 1
    # 11 points graph precision recall
    logger.info(f'plotting r-precision - {s}')
    name = '/'.join(compare)
    name_underscore = '_'.join([a.lower() for a in compare])
    data = r_precision(expected, results[compare[0]], results[compare[1]])
    plot_data(data,
        title=f'R-Precision {name}',
        xlabel='Query #',
        ylabel=f'R-Precision {name}',
        xlim=[0, 101],
        filename=f'{output_dir}/rprecision_{name_underscore}_{s}.pdf',
        graph=plt.bar)
    logger.info(f'saving r-precision data...')
    save_data_in_csv(data, f'{output_dir}/rprecision_{name_underscore}_{s}.csv')
    s += 1

    for c in compare:
        n_queries = len(results[c])
        stemmer = c.lower()
        get_filename = lambda name, extension: f'{output_dir}/{name}_{stemmer}_{s}.{extension}'
        # 11 points graph precision recall
        logger.info(f'plotting 11points {stemmer} - {s}')
        data = eleven_points_graph(expected, results[c])
        plot_data(data,
            title=f'11 points Precision x Recall ({stemmer} - média de {n_queries} queries)',
            xlabel='Revocação',
            ylabel='Precisão',
            xlim=[0, 1],
            filename=get_filename('11points', 'pdf'))
        logger.info(f'saving 11points {stemmer} data...')
        save_data_in_csv(data, get_filename('11points', 'csv'))
        s += 1

        # f1
        logger.info(f'plotting f1 {stemmer} - {s}')
        data = f1(expected, results[c])
        plot_data(data,
            title=f'F1 score ({stemmer}) - média de {n_queries} queries AVG: {data[1, :].mean().round(2)})',
            xlabel='Query #',
            ylabel='F1',
            xlim=[0, 101],
            filename=get_filename('f1', 'pdf'),
            graph=plt.bar)
        logger.info(f'saving f1 {stemmer} data...')
        save_data_in_csv(data, get_filename('f1', 'csv'))
        s += 1

        # precision@5
        logger.info(f'plotting precision@5 {stemmer} - {s}')
        data = precision_at(5, expected, results[c])
        plot_data(data,
            title=f'Precision@5 ({stemmer}) - AVG: {data[1, :].mean().round(2)}',
            xlabel='Query #',
            ylabel='Precisão',
            xlim=[0, 101],
            filename=get_filename('precision_at_5', 'pdf'),
            graph=plt.bar)
        logger.info(f'saving precision_at_5 {stemmer} data...')
        save_data_in_csv(data, get_filename('precision_at_5', 'csv'))
        s += 1

        # precision@10
        logger.info(f'plotting precision@10 {stemmer} - {s}')
        data = precision_at(10, expected, results[c])
        plot_data(data,
            title=f'Precision@10 ({stemmer}) - AVG: {data[1, :].mean().round(2)}',
            xlabel='Query #',
            ylabel='Precisão',
            xlim=[0, 101],
            filename=get_filename('precision_at_10', 'pdf'),
            graph=plt.bar)
        logger.info(f'saving precision_at_10 {stemmer} data...')
        save_data_in_csv(data, get_filename('precision_at_10', 'csv'))
        s += 1

        # MAP
        logger.info(f'plotting map {stemmer} - {s}')
        data = avg_precision(expected, results[c])
        plot_data(data,
            title=f'Average precision ({stemmer}) - MAP: {data[1, :].mean().round(2)}',
            xlabel='Query #',
            ylabel='Precisão média',
            xlim=[0, 101],
            filename=get_filename('avg_precision_map', 'pdf'),
            graph=plt.bar)
        logger.info(f'saving avg_precision_map {stemmer} data...')
        save_data_in_csv(data, get_filename('avg_precision_map', 'csv'))
        s += 1

        # MRR
        logger.info(f'plotting mrr {stemmer} - {s}')
        data = reciprocal_rank(expected, results[c])
        plot_data(data,
            title=f'Reciprocal rank score ({stemmer}) - MRR: {data[1, :].mean().round(2)}',
            xlabel='Query #',
            ylabel='Reciprocal rank',
            xlim=[0, 101],
            filename=get_filename('reciprocal_rank_mrr', 'pdf'),
            graph=plt.bar)
        logger.info(f'saving reciprocal_rank_mrr {stemmer} data...')
        save_data_in_csv(data, get_filename('reciprocal_rank_mrr', 'csv'))
        s += 1

        # DCG
        logger.info(f'plotting dcg {stemmer} - {s}')
        normalized, non_normalized = normalized_discounted_cumulative_gain(expected, results[c], 10)
        plot_data(non_normalized,
            title=f'Discounted cumulative gain ({stemmer} - média de {n_queries} queries)',
            xlabel='p',
            ylabel='DCG',
            xlim=[1, 10],
            filename=get_filename('dcg', 'pdf'))
        logger.info(f'saving dcg {stemmer} data...')
        save_data_in_csv(data, get_filename('dcg', 'csv'))
        s += 1

        # NDCG
        logger.info(f'plotting ndcg {stemmer} - {s}')
        plot_data(normalized,
            title=f'Normalized discounted cumulative gain ({stemmer} - média de {n_queries} queries)',
            xlabel='p',
            ylabel='NDCG',
            xlim=[1, 10],
            filename=get_filename('ndcg', 'pdf'))
        logger.info(f'saving ndcg {stemmer} data...')
        save_data_in_csv(data, get_filename('ndcg', 'csv'))
        s += 1

if __name__ == '__main__':
    main()

