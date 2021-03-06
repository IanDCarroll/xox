import unittest
from Training.observer_abilities import *

class ObserverTestCase(unittest.TestCase):

    def setUp(self):
        self.observer = Observer()
        self.mock_4x4_board = [  1, 0, 0,10,
                                 0, 1,10, 0,
                                 0,10, 1, 0,
                                10, 0, 0, 1 ]
        self.expected_4x4_analysis = [ 11,11,11,11, 
                                       11,11,11,11, 
                                        4,40 ]

        self.mock_board = [1,0,10, 1,10,0, 1,10,1]
        self.expected_analysis = [11,11,12, 3,20,11, 12,21]
        self.expected_rows = [11,11,12]
        self.expected_cols = [3,20,11]
        self.expected_diags = [12,21]
        self.expected_1st_value = 12
        self.expected_2nd_value = 21

    def test_get_board_size_3(self):
        test = self.observer.get_board_size(self.mock_board)
        self.assertEqual(test, 3)

    def test_get_board_size_4(self):
        test = self.observer.get_board_size(self.mock_4x4_board)
        self.assertEqual(test, 4)

    def test_scan_board_can_handle_4x4_boards(self):
        test = self.observer.scan_board(self.mock_4x4_board)
        self.assertEqual(test, self.expected_4x4_analysis)

    def test_scan_board_returns_analyzed_list(self):
        test_yields = self.observer.scan_board(self.mock_board)
        self.assertEqual(test_yields, self.expected_analysis)

    def test_scan_rows_returns_analyzed_list(self):
        test_yields = self.observer.scan_rows(self.mock_board)
        self.assertEqual(test_yields, self.expected_rows)

    def test_scan_cols_returns_analyzed_list(self):
        test_yields = self.observer.scan_cols(self.mock_board)
        self.assertEqual(test_yields, self.expected_cols)

    def test_scan_diags_returns_analyzed_list(self):
        test_yields = self.observer.scan_diags(self.mock_board)
        self.assertEqual(test_yields, self.expected_diags)

    def test_scan_first_diag_returns_analyzed_value(self):
        test_yields = self.observer.scan_1st_diag(self.mock_board)
        self.assertEqual(test_yields, self.expected_1st_value)

    def test_scan_second_diag_returns_analyzed_value(self):
        test_yields = self.observer.scan_2nd_diag(self.mock_board)
        self.assertEqual(test_yields, self.expected_2nd_value)

if __name__ == '__main__':
    unittest.main()
