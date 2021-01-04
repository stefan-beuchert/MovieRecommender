import unittest
import pandas as pd
import numpy as np

from modeling.model_training import create_similarity_matrix


class ModelingTest(unittest.TestCase):

    def test_similartiy_matrix_creation(self):
        input_df = pd.DataFrame({'C1': ["AB", "BA"]}, columns=['C1'])
        input_target_feature = 'C1'
        output = create_similarity_matrix(input_df, input_target_feature)

        expected_output = np.array([[1., 0.], [0., 1.]])

        self.assertTrue((output == expected_output).all())
