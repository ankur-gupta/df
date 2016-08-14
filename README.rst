simpledf
--------

An easier to use apply function for pandas groupby operations involving a
custom function. See
`Jupyter notebook example <https://github.com/ankur-gupta/simpledf/blob/master/simpledf/examples/apply_example.ipynb>`_
that verifies the complexity of selection sort.

============
Installation
============

This package exists on `pypi <https://pypi.python.org/pypi/simpledf>`_.
You can install it using `pip`::

    pip install simpledf

============
Demo
============

Here is a quick demo of how this package works::

    >>> import simpledf as sdf
    >>> import pandas as pd
    >>> import numpy as np
    >>> x = pd.DataFrame({'Data': [1, 2, 3], 'Group': ['A', 'B', 'B']})
    >>> def f(y):
            y['Mean'] = np.mean(y['Data'].values)
            return y

    >>> z = sdf.apply(x.groupby('Group'), f)
    >>> print z


