from .progressbars import display_multi_progress
from ipyparallel import Client


def execute_in_parallel(func, list_):
    c = Client()
    lbview = c.load_balanced_view()
    results = lbview.map_async(func, list_)
    display_multi_progress(results, list_)
    return results
