import unittest
from src.app import index


class AppTest(unittest.TestCase):

    def test_index(self):

        self.assertEqual(index(), "Hello World!")


if __name__ == '__main__':
    unittest.main()
