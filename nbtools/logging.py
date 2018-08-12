import logging
import sys


def setup_live_logging(module, level, fname=None):
    logger = logging.getLogger(module)
    ch = logging.StreamHandler(sys.stderr)
    fmt = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
    ch.setFormatter(fmt)
    logger.addHandler(ch)
    if fname is not None:
        fh = logging.FileHandler(fname)
        fh.setLevel(level)
        fh.setFormatter(fmt)
        logger.addHandler(fh)
    logger.setLevel(level)

    return logger
