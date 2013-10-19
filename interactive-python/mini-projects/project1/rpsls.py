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

    >>> numer_to_name(0)
    rock
    >>> is_valid_word(['RED','GREEN','BLUE','YELLOW'],'MAGENTA'))
    False
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
    # fill in your code below

    # convert name to number using if/elif/else
    # don't forget to return the result!
    number = ""
    return number


def rpsls(name): 
    # fill in your code below

    # convert name to player_number using name_to_number

    # compute random guess for comp_number using random.randrange()

    # compute difference of player_number and comp_number modulo five

	# use if/elif/else to determine winner

    # convert comp_number to name using number_to_name
    
    # print results
    print('rock')

class TestRPSLS(unittest.TestCase):
    
    def setUp(self):
        """ (self) -> None

        Setup scaffolding for the tests
        """
        print('setup')
        
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
    def test_number_to_name_rock(self):
        self.assertEqual(number_to_name(0),'rock')
        
    def test_number_to_name_Spock(self):
        self.assertEqual(number_to_name(1),'Spock')
        
    def test_number_to_name_paper(self):
        self.assertEqual(number_to_name(2),'paper')
        
    def test_number_to_name_lizard(self):
        self.assertEqual(number_to_name(3),'lizard')
        
    def test_number_to_name_scissors(self):
        self.assertEqual(number_to_name(4),'scissors')


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


