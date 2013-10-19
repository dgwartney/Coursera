# Rock-paper-scissors-lizard-Spock template

import unittest
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def number_to_name(number):
    """ (int) -> str

    Return the name of the hand given the number of the hand

    >>> number_to_name(0)
    rock
    >>> number_to_name(1)
    Spock
    >>> number_to_name(2)
    paper
    >>> number_to_name(3)
    lizard
    >>> number_to_name(4)
    Scissors
    >>> number_to_name(100)
    unknown
    >>> number_to_name(-1)
    unknown

    """


    # fill in your code below
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!

    if (number == 0):
        name = 'rock'
    elif (number == 1):
        name = 'Spock'
    elif (number == 2):
        name = 'paper'
    elif (number == 3):
        name = 'lizard'
    elif (number == 4):
        name = 'scissors'
    else:
        name = 'unknown'

    return name

    
def name_to_number(name):
    """ (str) -> int

    Converts the input name to its corresponding number
    
    >>> name_to_number('rock')
    rock
    >>> name_to_number('Spock')
    Spock
    >>> name_to_number('paper')
    paper
    >>> name_to_number('lizard')
    lizard
    >>> name_to_number('scissors')
    Scissors
    >>> name_to_number('thumb')
    9999
    >>> name_to_number('hand')
    """
    # fill in your code below

    # convert name to number using if/elif/else
    # don't forget to return the result!

    if (name == 'rock'):
        number = 0
    elif (name == 'Spock'):
        number = 1
    elif (name == 'paper'):
        number = 2
    elif (name == 'lizard'):
        number = 3
    elif (name == 'scissors'):
        number = 4
    else:
        number = 9999

    return number

def game_result(player,computer):
    """ (int,int) -> int
    """
    return (player - computer) % 5

def rpsls(name):
    """ (str) -> None

    Simulates the game of rock,Spock, paper, lizard. The input name
    is the players hand. A random hand is selected and compared against
    the player and output is provide on the winner.

    >>> rpsls('rock')
    Player chooses rock
    Computer chooses scissors
    Player wins!
    >>> rpsls('Spock')
    Player chooses Spock
    Computer chooses lizard
    Computer wins!
    >>> rpsls('paper')
    Player chooses paper
    Computer chooses lizard
    Computer wins!
    >>> rpsls('lizard')
    Player chooses lizard
    Computer chooses scissors
    Computer wins!
    >>> rpsls('scissors')
    Player chooses scissors
    Computer chooses Spock
    Computer wins!
    """

    # convert name to player_number using name_to_number
    player_number = name_to_number(name)

    # compute random guess for comp_number using random.randrange()
    computer_number = random.randrange(0,5)

    # compute difference of player_number and comp_number modulo five
    result = (player_number - computer_number) % 5
    
    # use if/elif/else to determine winner
    if (result == 0):
        outcome = 'Player and Computer tie!'
    elif (result >= 1 and result <= 2):
        outcome ='Player wins!'
    else:
        outcome = 'Computer wins!'
    
    # convert comp_number to name using number_to_name
    computer_name = number_to_name(computer_number)
    
    # print results
    print('Player chooses ' + name)
    print('Computer chooses ' + computer_name)
    print(outcome)

class TestRPSLS(unittest.TestCase):
    
    def setUp(self):
        """ (self) -> None

        Setup scaffolding for the tests
        """
        random.seed(1)

#
# Create our test cases using this mapping:
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

#
# Test cases for number_to_name()
#
    def test_number_to_name_0(self):
        self.assertEqual(number_to_name(0),'rock')
        
    def test_number_to_name_1(self):
        self.assertEqual(number_to_name(1),'Spock')
        
    def test_number_to_name_2(self):
        self.assertEqual(number_to_name(2),'paper')
        
    def test_number_to_name_3(self):
        self.assertEqual(number_to_name(3),'lizard')
        
    def test_number_to_name_4(self):
        self.assertEqual(number_to_name(4),'scissors')

    def test_number_to_name_100(self):
        self.assertEqual(number_to_name(100),'unknown')
        
    def test_number_to_name_negative1(self):
        self.assertEqual(number_to_name(-1),'unknown')


#
# Test cases for name_to_number()
#
    def test_name_to_number_rock(self):
        self.assertEqual(name_to_number('rock'),0)

    def test_name_to_number_Spock(self):
        self.assertEqual(name_to_number('Spock'),1)

    def test_name_to_number_paper(self):
        self.assertEqual(name_to_number('paper'),2)

    def test_name_to_number_lizard(self):
        self.assertEqual(name_to_number('lizard'),3)

    def test_name_to_number_scissors(self):
        self.assertEqual(name_to_number('scissors'),4)

    def test_name_to_number_thumb(self):
        self.assertEqual(name_to_number('thumb'),9999)
        
    def test_name_to_number_hand(self):
        self.assertEqual(name_to_number('hand'),9999)


##3
##0
##1
##3
##0
    def test_rpsls_rock(self):
        result = "Player chooses rock\nComputer chooses lizard\nComputer wins1"
        self.assertEqual(rpsls("rock"),result)
        
    def test_rpsls_rock(self):
        result = "Player chooses Spock\nComputer chooses rock\nComputer wins!"
        self.assertEqual(rpsls("rock"),result)
        

#
# Test cases for rpsls
#



def run_unit_tests():
    """ (None) -> None

    Runs the unit tests to validate code
    """
    unittest.main()

# Run our unit tests
run_unit_tests()

# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


