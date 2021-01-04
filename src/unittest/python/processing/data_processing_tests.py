import unittest
import pandas as pd

from processing.data_processing import remove_stopwords, clean_data


class ProcessingTest(unittest.TestCase):

    def test_stop_word_removal(self):

        input_string = """Any fool can write code that a computer can understand 
        Good programmers write code that humans can understand"""
        input_stop_words = ['code', 'that', 'a', 'can']
        expected_result = "Any fool write computer understand Good programmers write humans understand"

        result = remove_stopwords(input_string, input_stop_words)

        self.assertEqual(result, expected_result)

    def test_whole_data_cleaning(self):

        input_df = pd.DataFrame({'C1': ["I am a dog.", "I am a cat!"],
                                 'C2': ["I am a useless column", "Yes I am"]},
                                columns=['C1', 'C2'])
        input_important_columns = ['C1']
        input_target_feature = 'C1'
        input_unwanted_characters = ['.', '!']
        input_stop_word_language = 'en'

        output = clean_data(input_df, input_important_columns, input_target_feature,
                            input_unwanted_characters, input_stop_word_language)

        expected_output = pd.DataFrame({'C1': ["dog", "cat"]},
                                       columns=['C1'])

        self.assertTrue(output.equals(expected_output))




