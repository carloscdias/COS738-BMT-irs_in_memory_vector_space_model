#!python3
import logging
import logging.config
from configparser import ConfigParser

PROGRAM_CONFIG_FILENAME = 'config.ini'
LOGGING_CONFIG_FILENAME = 'logging.ini'
config = ConfigParser()
config.read(SEARCH_ENGINE_CFG)
logging.config.fileConfig(LOGGING_CONFIG_FILENAME)
logger = logging.getLogger(__name__)

def main():
    logger.info('starting "busca"...')
    logger.info('reading seach engine configuration...')
    print(config['DEFAULT']['MODELO'])
    print(config['DEFAULT']['RESULTADOS'])

if __name__ == '__main__':
    main()

