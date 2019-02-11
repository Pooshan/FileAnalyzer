import unittest
from src_files import fileAnalyzer



class TestFileAnalyzer(unittest.TestCase):
    def test_positive_case(self):
        result=fileAnalyzer.find_n_most_frequent_word('../src_files/test_few_words.txt',5)
        self.assertEqual(len(result), 4)
        self.assertEqual(result['hello'], 3)

    def test_negative_case(self):
        """
        Test with empty input file
        :return:
        """
        result=fileAnalyzer.find_n_most_frequent_word('../src_files/emptyfile.txt',5)
        self.assertEqual(len(result), 0)

if __name__ == '__main__':
    unittest.main()

