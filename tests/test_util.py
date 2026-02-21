import argparse
import unittest

from lain_upload.util import expire_after_type


class ExpireAfterTypeTests(unittest.TestCase):
    def test_accepts_hour_suffix(self):
        self.assertEqual(expire_after_type("12h"), "12h")

    def test_rejects_invalid_values(self):
        invalid_values = ["12", "h", "1d", "01H", "-1h"]
        for value in invalid_values:
            with (
                self.subTest(value=value),
                self.assertRaises(argparse.ArgumentTypeError),
            ):
                expire_after_type(value)


if __name__ == "__main__":
    unittest.main()
