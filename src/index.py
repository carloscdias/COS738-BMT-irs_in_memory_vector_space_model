#!python3
from utils import init_irs

def main():
    config, logger = init_irs('INDEX')
    logger.info('starting "index"...')

    logger.info('reading index configuration...')
    inverted_list_filename = config['LEIA']
    output_filename = config['ESCREVA']

    logger.info('done processing "index"...')

if __name__ == '__main__':
    main()

