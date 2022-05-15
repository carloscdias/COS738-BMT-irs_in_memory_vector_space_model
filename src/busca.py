#!python3
import csv
import numpy as np
from nltk.tokenize import word_tokenize
from utils import init_irs, get_stemmer

RANK_LIMIT = 10

def main():
    config, logger = init_irs('BUSCA')
    logger.info('starting "busca"...')

    logger.info('reading search engine configuration...')
    model_filename = config['MODELO']
    query_filename = config['CONSULTAS']
    results_filename = config['RESULTADOS']
    stemmer_option = config['STEMMER']
    stemmer = get_stemmer(stemmer_option)

    logger.info(f'loading model in "{model_filename}"')
    with open(model_filename, 'rb') as model:
        all_terms = np.load(model)
        all_documents = np.load(model)
        term_document_matrix = np.load(model)

    T = len(all_terms)
    N = len(all_documents)
    queries = []
    all_queries = np.empty((T, 0))
    logger.info(f'parsing querys in "{query_filename}"')
    with open(query_filename, newline='') as query:
        query_csv = csv.reader(query, delimiter=';')
        header = query_csv.__next__()
        for query_number, query_text in query_csv:
            queries.append(query_number)
            query = np.zeros((T, 1))
            for w in word_tokenize(query_text):
                result = np.where(all_terms == stemmer.stem(w))
                if len(result[0]) > 0:
                    index = result[0][0]
                    query[index, 0] = 1
            all_queries = np.concatenate([all_queries, query], axis=1)

    logger.info('calculating similarity...')
    inner_product = np.dot(all_queries.transpose(), term_document_matrix)
    norm_query = np.linalg.norm(all_queries, axis=0).reshape(-1, 1)
    norm_model = np.linalg.norm(term_document_matrix, axis=0).reshape(1, -1)
    norm_product = np.dot(norm_query, norm_model)
    results = inner_product/norm_product
    sorted_results = np.argsort(-results)

    logger.info(f'writing results in "{results_filename}"')
    with open(results_filename, 'w', newline='') as results_file:
        results_csv = csv.writer(results_file, delimiter=';')

        for i, query in enumerate(queries):
            for j in range(RANK_LIMIT):
                order = j + 1
                document_index = sorted_results[i, j]
                document = all_documents[document_index]
                distance = results[i, document_index]
                results_csv.writerow([query, str([order, document, distance])])

    logger.info('done processing "busca"...')

if __name__ == '__main__':
    main()

