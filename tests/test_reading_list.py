import unittest
from unittest.mock import patch, mock_open
from random import choice

from reading_list import clean_line, process_line, STATUS_READ, STATUS_READING, STATUS_DNF, STATUS_TO_READ

class TestReadingList(unittest.TestCase):
    def test_clean_line(self):

        line = "- [ ] [[Book Title]] by Author*\n"
        cleaned = clean_line(line)
        self.assertEqual(cleaned, "Book Title by Author")

        line = "- [/] [[Another Book]] by Another Author\n"
        cleaned = clean_line(line)
        self.assertEqual(cleaned, "Another Book by Another Author")

        line = "\n"
        cleaned = clean_line(line)
        self.assertEqual(cleaned, "")

    def test_process_line(self):
        counters = {
            "read": 0,
            "dnf": 0,
            "to_read": 0,
            "total": 0,
            "currently_reading": None,
        }
        books_to_read = []

        line = "- [x] [[The Great Gatsby]] - F. Scott Fitzgerald\n"
        process_line(line, counters, books_to_read)
        self.assertEqual(counters["read"], 1)
        self.assertEqual(counters["total"], 1)
        self.assertEqual(counters["currently_reading"], None)
        self.assertEqual(books_to_read, [])

        line = "- [/] [[The Divine Comedy]] - Dante Alighieri\n"
        process_line(line, counters, books_to_read)
        self.assertEqual(counters["currently_reading"], "The Divine Comedy - Dante Alighieri")
        self.assertEqual(counters["total"], 2)
        self.assertEqual(books_to_read, [])

        line = "- [ ] [[Scouts Out]] - Ryan Robicheaux\n"
        process_line(line, counters, books_to_read)
        self.assertEqual(counters["to_read"], 1)
        self.assertEqual(counters["total"], 3)
        self.assertEqual(books_to_read, ["Scouts Out - Ryan Robicheaux"])

        line = "- [-] [[Moby Dick]] - Herman Melville\n"
        process_line(line, counters, books_to_read)
        self.assertEqual(counters["dnf"], 1)
        self.assertEqual(counters["total"], 4)
        self.assertEqual(books_to_read, ["Scouts Out - Ryan Robicheaux"])

    @patch("builtins.open", mock_open(read_data="- [x] [[Book 1]]\n- [/] [[Book 2]]\n- [ ] [[Book 3]]\n"))
    def test_main_with_mock_file(self):
        from reading_list import main

        with patch("builtins.print") as mock_print:
            main()

            mock_print.assert_any_call("Currently reading: Book 2")
            mock_print.assert_any_call("You read: 1 out of 3 books.")
            mock_print.assert_any_call("Did not finish: 0")
            mock_print.assert_any_call("Randomly picked next book: Book 3")

    @patch("builtins.open", mock_open(read_data=""))
    def test_main_with_empty_file(self):
        from reading_list import main

        with patch("builtins.print") as mock_print:
            main()

            mock_print.assert_any_call("You are not currently reading any book.")
            mock_print.assert_any_call("You read: 0 out of 0 books.")
            mock_print.assert_any_call("Did not finish: 0")
            mock_print.assert_any_call("No books to read in the list.")

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_main_with_missing_file(self, mock_open):
        from reading_list import main

        with patch("builtins.print") as mock_print:
            main()

            mock_print.assert_called_with("Error: The file 'READING LIST.md' was not found. Please ensure the file exists.")

if __name__ == "__main__":
    unittest.main()