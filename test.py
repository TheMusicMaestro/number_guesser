import unittest
from unittest.mock import patch, mock_open
from game import is_int
from stats import view_stats, reset_stats
import os


class TestIsInt(unittest.TestCase):
    def test_is_int_true(self):
        self.assertTrue(is_int("10"))

    def test_is_int_false(self):
        self.assertFalse(is_int("abc"))

    def test_is_int_out_of_range_positive(self):
        self.assertTrue(is_int("101"))

    def test_is_int_out_of_range_negative(self):
        self.assertTrue(is_int("0"))

    def test_is_int_non_integer(self):
        self.assertFalse(is_int("abc"))

    def test_is_int_less_than_one(self):
        self.assertTrue(is_int("0"))

    def test_is_int_greater_than_100(self):
        self.assertTrue(is_int("101"))


class TestViewStats(unittest.TestCase):
    @patch("builtins.print")
    @patch("builtins.open", new_callable=mock_open, read_data="5\n3\n7")
    def test_view_stats_with_data(self, mock_file, mock_print):
        view_stats()
        mock_print.assert_any_call("\n------ Game Statistics ------")
        mock_print.assert_any_call("Record Lowest Guess: 5\n3\n7")
        mock_print.assert_any_call("Total Number of Games Played: 3")
        mock_print.assert_any_call("Average Number of Guesses per Game: 5.00")
        mock_print.assert_any_call("-----------------------------\n")

    @patch("builtins.print")
    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_view_stats_no_data(self, mock_file, mock_print):
        view_stats()
        mock_print.assert_any_call("\n------ Game Statistics ------")
        mock_print.assert_any_call("No record set yet.")
        mock_print.assert_any_call("No games played yet.")
        mock_print.assert_any_call("-----------------------------\n")


class TestResetStats(unittest.TestCase):
    @patch("os.remove")
    @patch("builtins.print")
    @patch("inquirer.confirm", return_value=True)
    def test_reset_stats_confirmed(self, mock_confirm, mock_print, mock_remove):
        reset_stats()
        mock_remove.assert_any_call("record.txt")
        mock_remove.assert_any_call("history.txt")
        mock_print.assert_any_call("Stats have been reset.\n")

    @patch("os.remove")
    @patch("builtins.print")
    @patch("inquirer.confirm", return_value=False)
    def test_reset_stats_cancelled(self, mock_confirm, mock_print, mock_remove):
        reset_stats()
        mock_remove.assert_not_called()
        mock_print.assert_any_call("Stats reset cancelled.\n")


if __name__ == "__main__":
    unittest.main()
