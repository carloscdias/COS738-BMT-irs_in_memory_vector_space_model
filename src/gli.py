#!python3
import re
from xml.etree import ElementTree
import unidecode
import csv
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
from utils import init_irs, get_stemmer

nltk.download('stopwords')

def main():
    config, logger = init_irs('GLI')
    logger.info('starting "gli"...')

    logger.info('reading gli configuration...')
    xml_filenames = re.split('\s*,\s*', config['LEIA'])
    inverted_list_filename = config['ESCREVA']
    stemmer_option = config['STEMMER']
    stemmer = get_stemmer(stemmer_option)

    inverted_list = defaultdict(list)
    stopwords_upper = [w.upper() for w in stopwords.words('english')]
    empty_articles = []
    for xml in xml_filenames:
        logger.info(f'reading xml file "{xml}"')
        root = ElementTree.parse(xml).getroot()
        for e in root.findall('RECORD'):
            record_num = e.find('RECORDNUM').text.strip()
            abstract = ''
            if e.findall('ABSTRACT'):
                abstract = e.find('ABSTRACT').text
            elif e.findall('EXTRACT'):
                logger.warning(f'ABSTRACT for record {record_num} not found, using EXTRACT instead')
                abstract = e.find('EXTRACT').text

            if not abstract:
                logger.error(f'empty text content for article {record_num} in {xml}')
                empty_articles.append(record_num)
                continue

            text = unidecode.unidecode(abstract.replace(';', '').strip().upper())
            for w in word_tokenize(text):
                if w not in stopwords_upper:
                    inverted_list[stemmer.stem(w)].append(record_num)

    logger.warning(f'{len(empty_articles)} empty articles: {empty_articles}')
    logger.info(f'writing xml file "{inverted_list_filename}"')
    with open(inverted_list_filename, 'w', newline='') as inverted_list_file:
        inverted_list_csv = csv.writer(inverted_list_file, delimiter=';')

        for w, l in inverted_list.items():
            inverted_list_csv.writerow([w, str(l)])

    logger.info('done processing "gli"...')

if __name__ == '__main__':
    main()

