import unittest
from unittest.mock import patch
import Task1 as task1

class Testtask1(unittest.TestCase):

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['Alice', 'Bob', ''])
    def test_main_multiple_inputs(self, mock_input, mock_print):
        task1.main()
        task1.main()
        task1.main()

        mock_print.assert_has_calls([
            unittest.mock.call('Hi, Alice'),
            unittest.mock.call('Hi, Bob'),
            unittest.mock.call('Hi, ')
        ])

if __name__ == '__main__':
    unittest.main()