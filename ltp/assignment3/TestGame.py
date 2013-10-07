##import a3
##
##def test_is_valid_word():
##    result = False
##        
##    result = is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TO')
##    if result == False:
##        print("
##    >>> is_valid_word(['RED','GREEN','BLUE','YELLOW'],'MAGENTA'))
##    False
##
##    return result

import unittest
import a3

class TestGame(unittest.TestCase):

    def setUp(self):
        print("setUp")

    def test_is_valid_word(self):
        self.assertTrue(a3.is_valid_word(['RED','GREEN','BLUE','YELLOW'],'MAGENTA'))



##    def test_shuffle(self):
##        # make sure the shuffled sequence does not lose any elements
##        random.shuffle(self.seq)
##        self.seq.sort()
##        self.assertEqual(self.seq, range(10))
##
##        # should raise an exception for an immutable sequence
##        self.assertRaises(TypeError, random.shuffle, (1,2,3))
##
##    def test_choice(self):
##        element = random.choice(self.seq)
##        self.assertTrue(element in self.seq)
##
##    def test_sample(self):
##        with self.assertRaises(ValueError):
##            random.sample(self.seq, 20)
##        for element in random.sample(self.seq, 5):
##            self.assertTrue(element in self.seq)

if __name__ == '__main__':
    unittest.main()
