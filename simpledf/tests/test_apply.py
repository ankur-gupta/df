import simpledf as sdf
import pandas as pd
import numpy as np
from unittest import TestCase


def f(y):
    ''' A custom function that changes the shape of dataframes '''
    y['Mean'] = np.mean(y['Data'].values)
    return y


class TestApply(TestCase):
    def test_apply_basic(self):
        x = pd.DataFrame({'Data': [1, 2, 3], 'Group': ['A', 'B', 'B']})
        z = sdf.apply(x.groupby('Group'), f)
        self.assertTrue(z.shape == (3, 3))
        self.assertTrue(z.columns[0] == 'Data')
        self.assertTrue(z.columns[1] == 'Group')
        self.assertTrue(z.columns[2] == 'Mean')
        self.assertTrue(np.all(z['Data'].values == np.array([1, 2, 3])))
        self.assertTrue(np.all(z['Group'].values == np.array(['A', 'B', 'B'])))
        self.assertTrue(np.all(z['Mean'].values == np.array([1.0, 2.5, 2.5])))


