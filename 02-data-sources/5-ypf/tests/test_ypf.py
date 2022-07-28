import unittest

class TestYPF(unittest.TestCase):
    def __init__(self, dataframe):
        self.result = dataframe

    def test_YPF_df_index_name_is_date(self):
        self.assertEqual(self.result.index_name, 'date')

    def test_YPF_df_index_is_timestamp(self):
        self.assertEqual(self.result.index_type, '<M8[ns]', "Check you converted the 'date' colummn into a `datetime`.")

    def test_YPF_df_columns(self):
        columns = {
        'Open', 'High', 'Low', 'Close', 'Volume', 'Dividends', 'Stock Splits'            }
        self.assertEqual(columns.issubset(set(self.result.columns)), True)
