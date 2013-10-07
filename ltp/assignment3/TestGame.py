import unittest
import a3

class TestGame(unittest.TestCase):

    def setUp(self):
        self.board1 = [['A', 'N', 'T', 'T'],
                       ['X', 'S', 'O', 'B']]
        self.board2 = [['R','G','B'],
                       ['C','Y','K']]
        self.board3 = [['A','B','C','D','E'],
                       ['F','G','H','I','J'],
                       ['K','L','M','N','O'],
                       ['P','Q','R','S','T'],
                       ['U','V','W','X','Y']]

        self.board4 = [['E','F','J','A','J','C','O','W','S','S'],
                       ['S','D','G','K','S','R','F','D','F','F'],
                       ['A','S','R','J','D','U','S','K','L','K'],
                       ['H','E','A','N','D','N','D','J','W','A'],
                       ['A','N','S','D','N','C','N','E','O','P'],
                       ['P','M','S','N','F','H','H','E','J','E'],
                       ['J','E','P','Q','L','Y','N','X','D','L']]
        self.word_list = ['CRUNCHY','COWS','EAT','GRASS']

            

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
        self.assertEqual(a3.make_str_from_column(self.board4, 2),'JGRASSP')

    def test_contains_word_in_row(self):
        self.assertTrue(a3.board_contains_word_in_row(self.board1,'SOB'))

    def test_contains_word_in_column(self):
        self.assertFalse(a3.board_contains_word_in_column(self.board1,'NO'))
        self.assertTrue(a3.board_contains_word_in_column(self.board1,'AX'))
        self.assertTrue(a3.board_contains_word_in_column(self.board1,'NS'))
        self.assertTrue(a3.board_contains_word_in_column(self.board2,'RC'))
        self.assertFalse(a3.board_contains_word_in_column(self.board2,'ZZ'))
        self.assertTrue(a3.board_contains_word_in_column(self.board4,'GRASS'))
        self.assertFalse(a3.board_contains_word_in_column(self.board4,'GRASY'))

    def test_board_contains_word(self):
        self.assertTrue(a3.board_contains_word(self.board1,'ANT'))
        self.assertTrue(a3.board_contains_word(self.board3,'ABC'))
        self.assertTrue(a3.board_contains_word(self.board4,'GRASS'))

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

    def test_num_words_on_board(self):

        self.assertEqual(a3.num_words_on_board(self.board1,['ANT']),1)
        self.assertEqual(a3.num_words_on_board(self.board1,['NO']),0)
        self.assertEqual(a3.num_words_on_board(self.board4,self.word_list),3)


    def test_read_words(self):
        words_file = open('wordlist1.txt','r')
        word_list = a3.read_words(words_file)

        for i in range(len(word_list)):
            self.assertEqual(word_list[i],self.word_list[i])
        

    def test_read_board(self):
        board_file = open('board1.txt','r')
        board = a3.read_board(board_file)

        # Check that number of rows match against our test fixture
        self.assertEqual(len(board),len(self.board4))

        # Check that number of columns match against our test fixture
        for r in range(len(board)):
            self.assertEqual(len(board[r]),len(self.board4[r]))

        # Check that each row/column values matches
        for r in range(len(board)):
            for c in range(len(board[r])):
                self.assertEqual(board[r][c],self.board4[r][c])





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
