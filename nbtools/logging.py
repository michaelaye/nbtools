import logging
import sys


def setup_live_logging(module, level):
    logger = logging.getLogger(module)
    ch = logging.StreamHandler(sys.stderr)
    fmt = logging.Formatter('%(name)s - %(message)s')
    ch.setFormatter(fmt)
    logger.addHandler(ch)
    logger.setLevel(level)
