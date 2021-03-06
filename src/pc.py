#!python3
from xml.etree import ElementTree
import unidecode
import csv
from utils import init_irs

QUERY_FILE_HEADER = ['QueryNumber', 'QueryText']
EXPECTED_FILE_HEADER = ['QueryNumber', 'DocNumber', 'DocVotes']

def main():
    config, logger = init_irs('PC')
    logger.info('starting "pc"...')

    logger.info('reading query engine configuration...')
    query_xml_filename = config['LEIA']
    query_filename = config['CONSULTAS']
    expected_filename = config['ESPERADOS']

    logger.info(f'reading query xml file "{query_xml_filename}"')
    root = ElementTree.parse(query_xml_filename).getroot()

    logger.info(f'writing output csv files "{query_filename}" and "{expected_filename}"')
    with open(query_filename, 'w', newline='') as query, open(expected_filename, 'w', newline='') as expected:
        query_csv = csv.writer(query, delimiter=';')
        query_csv.writerow(QUERY_FILE_HEADER)

        expected_csv = csv.writer(expected, delimiter=';')
        expected_csv.writerow(EXPECTED_FILE_HEADER)

        for e in root.findall('QUERY'):
            query_number = e.find('QueryNumber').text
            query_text_dirty = e.find('QueryText').text
            query_text = unidecode.unidecode(query_text_dirty.replace(';', '').strip().upper())
            query_csv.writerow([query_number, query_text])
            for i in e.findall('Records/Item'):
                doc_number = i.text
                score = i.get('score')
                doc_votes = len(score.replace('0', ''))
                expected_csv.writerow([query_number, doc_number, doc_votes])

    logger.info('done processing "pc"...')

if __name__ == '__main__':
    main()

