import logging
import sys

l_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'


def run_logger(level=logging.INFO):
    '''
    Run logger
    :param level: logger level 0 - 50
    '''
    formatter = logging.Formatter(l_format)
    logger = logging.getLogger()
    # Logger INFO
    info_handler = logging.StreamHandler(sys.stdout)
    info_handler.setLevel(level)
    info_handler.setFormatter(formatter)
    logger.addHandler(info_handler)
    # Logger ERROR
    err_handler = logging.StreamHandler(sys.stderr)
    err_handler.setLevel(logging.ERROR)
    err_handler.setFormatter(formatter)
    logger.addHandler(err_handler)

