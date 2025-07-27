import unittest
from unittest.mock import patch
import Number_Guessing as ng

class TestGuessingLogic(unittest.TestCase):
    def test_win_on_first_try(self):
        with patch('Number_Guessing.C_guess', return_value=5), \
             patch('Number_Guessing.P_guess', side_effect=[5]), \
             patch('builtins.print') as mock_print:
            ng.check_winner()
            mock_print.assert_any_call("You win!")
            mock_print.assert_any_call("You guessed the correct number!")

    def test_win_after_hint(self):
        with patch('Number_Guessing.C_guess', return_value=7), \
             patch('Number_Guessing.P_guess', side_effect=[1, 2, 6, 7]), \
             patch('builtins.print') as mock_print:
            ng.check_winner()
            mock_print.assert_any_call("You win! You guessed the correct number!")

if __name__ == '__main__':
    unittest.main()
