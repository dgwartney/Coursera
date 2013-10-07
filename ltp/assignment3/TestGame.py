import unittest
import a3

class TestGame(unittest.TestCase):

    def setUp(self):
        self.board1 = [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]
        self.board2 = [['R','G','B'],['C','Y','K']]
        self.board3 = [['A','B','C','D','E'],
                       ['F','G','H','I','J'],
                       ['K','L','M','N','O'],
                       ['P','Q','R','S','T'],
                       ['U','V','W','X','Y']]

    def test_is_valid_word_false(self):
        self.assertFalse(a3.is_valid_word(['RED','GREEN','BLUE','YELLOW'],'MAGENTA'))

    def test_is_valid_word_true(self):
        self.assertTrue(a3.is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TO'))

    def test_str_from_row(self):
        self.assertEqual(a3.make_str_from_row(self.board1, 0),'ANTT')
        self.assertEqual(a3.make_str_from_row(self.board2, 1),'CYK')

    def test_str_from_column(self):
        self.assertEqual(a3.make_str_from_column(self.board1, 1),'NS')
        self.assertEqual(a3.make_str_from_column(self.board2, 0),'RC')

    def test_contains_word_in_row(self):
        self.assertTrue(a3.board_contains_word_in_row(self.board1,'SOB'))

    def test_contains_word_in_column(self):
        self.assertFalse(a3.board_contains_word_in_column(self.board1,'NO'))
        self.assertTrue(a3.board_contains_word_in_column(self.board1,'AX'))
        self.assertTrue(a3.board_contains_word_in_column(self.board1,'NS'))
        self.assertTrue(a3.board_contains_word_in_column(self.board2,'RC'))
        self.assertFalse(a3.board_contains_word_in_column(self.board2,'ZZ'))

    def test_board_contains_word(self):
        self.assertTrue(a3.board_contains_word(self.board1,'ANT'))
        self.assertTrue(a3.board_contains_word(self.board3, 'ABC'))

    def test_word_score(self):
        self.assertEqual(a3.word_score('DRUDGERY'),16)
        self.assertEqual(a3.word_score('AX'),0)
        self.assertEqual(a3.word_score('CAT'),3)
        self.assertEqual(a3.word_score('ALBINO'),6)
        self.assertEqual(a3.word_score('ABALONE'),14)
        self.assertEqual(a3.word_score('AARDVARKS'),18)
        self.assertEqual(a3.word_score('ARRDWOLVES'),30)
        self.assertEqual(a3.word_score('WOLFBERRIES'),33)
        self.assertEqual(a3.word_score('DOGMATICALLY'),36)

    def test_update_score(self):
        player_info = ['Johnathon',4]
        word = 'CAT'
        a3.update_score(player_info,word)

        self.assertEqual(player_info[1],7)





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
