import unittest
from dictionary import make_dictionary

class TestDictionary(unittest.TestCase):
    def test_make_dictionary(self):
        self.assertTrue( {x: x*x for x in range(1,16)})

if __name__ == '__main__':
    unittest.main()