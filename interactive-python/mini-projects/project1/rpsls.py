# Rock-paper-scissors-lizard-Spock template


# Random number generation framework
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
        print("Invalid number setting name to unknown")

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
        print("Invalid name setting number to 9999")

    return number

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
    print('')
    print('Player chooses ' + name)
    print('Computer chooses ' + computer_name)
    print(outcome)

# Set seed before running so the sequence repeats for testing
##random.seed(1)

# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


