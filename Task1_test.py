import unittest
from unittest.mock import patch
import task1

class Testtask1(unittest.TestCase):

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['Alice', 'Bob', ''])
    def test_main_multiple_inputs(self, mock_input, mock_print):
        # First input
        task1.main()
        mock_print.assert_called_with('Hi, Alice')

        # Second input
        task1.main()
        mock_print.assert_called_with('Hi, Bob')

        # Third input (empty string)
        task1.main()
        mock_print.assert_called_with('Hi, ')

if __name__ == '__main__':
    unittest.main()
