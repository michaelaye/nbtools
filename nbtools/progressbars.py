"""Multiprocessing related Jupyter notebook tools."""
import sys
import time

from IPython.display import display
from ipywidgets import FloatProgress, IntProgress
from numpy import linspace
from tqdm import tqdm_notebook as tqdm


def progress_display(results, objectlist, sleep=10):
    while not results.ready():
        print("{:.1f} % done.".format(
            100 * results.progress / len(list(objectlist))))
        sys.stdout.flush()
        time.sleep(sleep)


def display_multi_progress(results, objectlist, sleep=1):
    with tqdm(objectlist) as prog:
        n_prev = 0
        while not results.ready():
            n_now = results.progress
            prog.update(n_now - n_prev)
            n_prev = n_now
            time.sleep(sleep)


class ListProgressBar(object):
    def __init__(self, objectlist, min_=0):
        self.list = objectlist
        self.prog = IntProgress(min=min_, max=len(list(objectlist)) - 1)
        display(self.prog)

    @property
    def value(self):
        return self.prog.value

    @value.setter
    def value(self, newvalue):
        self.prog.value = self.list.index(newvalue)


class IntProgressBar(object):
    def __init__(self, objectlist, min_=0):
        self.prog = IntProgress(min=min_, max=len(list(objectlist)) - 1)
        display(self.prog)

    @property
    def value(self):
        return self.prog.value

    @value.setter
    def value(self, newvalue):
        self.prog.value = newvalue


def float_progress(min_, max_):
    prog = FloatProgress(min=min_, max=max_)
    display(prog)
    for i in linspace(min_, max_, 100):
        time.sleep(0.1)
        prog.value = i
