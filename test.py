import unittest

from main import main

class MyTest(unittest.TestCase):

    def test(self):

        self.assertEqual(main(), 'hello world')

if __name__ == '__main__':
    
    unittest.main()