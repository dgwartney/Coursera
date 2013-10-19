import unittest
import contains

class TestGame(unittest.TestCase):

    def setUp(self):
        print('')


    def testTrue(self):
        s = 'moogah'
        d = {1: [70, 'blue'], 2: [1.24, 'moogah', 90], 3.14: [80, 100]}
        self.assertTrue(contains.contains(s,d))

    def testFalse(self):
        s = 'moogah'
        d = {'moogah': [1.24, 'frooble', 90], 3.14: [80, 100]}
        self.assertFalse(contains.contains(s,d))

if __name__ == '__main__':
    unittest.main()
 
