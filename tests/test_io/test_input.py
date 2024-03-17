import unittest
import pandas as pd
from app.io.input import turns_to_characters
from app.io.input import show_name_rgb


class TestTurnsToCharacters(unittest.TestCase):
    def test_with_valid_file(self):
        filename = "test_1.1.txt"
        with open(filename, "w") as f:
            f.write("SbahsuTgdv, rtyh")
        expected_output = "SBAHSUTGDV, RTYH"
        actual_output = turns_to_characters(filename)
        self.assertEqual(expected_output, actual_output)

    def test_with_empty_file(self):
        filename = "empty.txt"
        with open(filename, "w"):
            pass
        expected_output = ""
        actual_output = turns_to_characters(filename)
        self.assertEqual(expected_output, actual_output)

    def test_with_special_characters(self):
        filename = "special_chars.txt"
        with open(filename, "w") as f:
            f.write("Hello, w0rld!@#")
        expected_output = "HELLO, W0RLD!@#"
        actual_output = turns_to_characters(filename)
        self.assertEqual(expected_output, actual_output)


class ShowNameRGB(unittest.TestCase):
    def test_with_valid_csv(self):
        """Tests the function with a valid CSV file."""
        filename = "colors.csv"
        expected_data = {
            "Name": ["White", "Silver", "Gray", "Black"],
            "RGB": ["rgb(100,100,100)", "rgb(75,75,75)", "rgb(50,50,50)", "rgb(0,0,0)"]
        }
        df = pd.DataFrame(expected_data)
        df.to_csv(filename, index=False)

        try:
            df_result = show_name_rgb(filename)
            self.assertIsNotNone(df_result)
            self.assertEqual(df_result.shape, (4, 2))
            self.assertListEqual(list(df_result.columns), ["Name", "RGB"])
        finally:
            import os
            os.remove(filename)

    def test_with_empty_csv(self):
        filename = "empty.csv"
        df = pd.DataFrame(columns=["Name", "RGB"])
        df.to_csv(filename)
        self.assertEqual(show_name_rgb(filename).empty, True)

    def test_with_non_existent_csv(self):
        filename = "non_existent.csv"
        self.assertIsNone(show_name_rgb(filename))


if __name__ == '__main__':
    unittest.main()
