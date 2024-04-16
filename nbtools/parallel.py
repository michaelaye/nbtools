from .progressbars import display_multi_progress
from ipyparallel import Client
from dask import delayed, compute

# def execute_in_parallel(func, iterable):
#     """Use IPyparallel's load_balanced_view to execute in parallel.

#     Function will create a Client() object, a load_balanced_view and
#     a notebook widget based progressbar automatically. The processing
#     will be performed using the `map_async` method of the
#     load_balanced_view object.

#     Parameters
#     ----------
#     func : function
#         Function to call in parallel.
#     iterable : iterable
#         Iterable container that will be used as input for `func`.

#     Returns
#     -------
#     The results object from executing `lbview.map_async`.
#     """
#     c = Client()
#     lbview = c.load_balanced_view()
#     results = lbview.map_async(func, iterable)
#     display_multi_progress(results, iterable)
#     return results

def execute_in_parallel(func, iterable):
    lazys = []
    for item in iterable:
        lazys.append(delayed(func)(item))
    return compute(*lazys)