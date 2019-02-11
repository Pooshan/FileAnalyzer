import unittest
from src_files import fileAnalyzer



class TestFileAnalyzer(unittest.TestCase):
    def test_positive_case(self):
        result=fileAnalyzer.find_n_most_frequent_word('../test_few_words.txt',5)
        self.assertEqual(len(result), 4)
        self.assertEqual(result['hello'], 3)

    def test_negative_case(self):
        """

        :return:
        """
        result=fileAnalyzer.find_n_most_frequent_word('../test_few_words.txt',5)
        self.assertEqual(len(result), 4)
        self.assertEqual(result['hello'], 3)

if __name__ == '__main__':
    unittest.main()

